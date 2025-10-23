import os
import json
import logging
from typing import Any, Dict

from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import requests

# --- App setup ---
app = Flask(__name__, static_folder="static", static_url_path="")
CORS(app, resources={r"/*": {"origins": "*"}})

# --- Config / Environment ---
FLASK_ENV = os.getenv("FLASK_ENV", "production")
THIRD_PARTY_API_URL = os.getenv("THIRD_PARTY_API_URL", "https://jsonplaceholder.typicode.com/todos/1")
EXTERNAL_API_KEY = os.getenv("EXTERNAL_API_KEY")  # optional example

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("api-testing")


# --- Utility ---
def _ok(data: Any, status: int = 200):
    return jsonify({"ok": True, "data": data}), status

def _err(message: str, status: int = 400, detail: Dict[str, Any] | None = None):
    payload = {"ok": False, "error": {"message": message}}
    if detail:
        payload["error"]["detail"] = detail
    return jsonify(payload), status


# --- Routes ---
@app.route("/")
def root():
    # Serve the front-end page
    return send_from_directory(app.static_folder, "index.html")

@app.route("/healthz")
def healthz():
    return _ok({"status": "healthy", "env": FLASK_ENV})

@app.route("/api/echo", methods=["POST"])
def echo():
    try:
        payload = request.get_json(force=True, silent=False)
    except Exception:
        return _err("Invalid JSON body.", 400)
    return _ok({"you_sent": payload})

@app.route("/api/ping", methods=["GET"])
def ping():
    return _ok("pong")

@app.route("/api/calc", methods=["GET"])
def calc():
    """
    Example query: /api/calc?a=5&b=7
    """
    try:
        a = float(request.args.get("a", "0"))
        b = float(request.args.get("b", "0"))
    except ValueError:
        return _err("Parameters 'a' and 'b' must be numbers.", 400)
    return _ok({"a": a, "b": b, "sum": a + b})

@app.route("/api/external", methods=["GET"])
def external():
    """
    Example "call another API" endpoint.
    Reads optional API key from env (EXTERNAL_API_KEY).
    """
    headers = {}
    if EXTERNAL_API_KEY:
        headers["Authorization"] = f"Bearer {EXTERNAL_API_KEY}"

    try:
        resp = requests.get(
            THIRD_PARTY_API_URL,
            headers=headers,
            timeout=10,
        )
        resp.raise_for_status()
        # Try to parse as JSON, otherwise return text
        try:
            data = resp.json()
        except json.JSONDecodeError:
            data = {"raw": resp.text}
        return _ok({"source": THIRD_PARTY_API_URL, "result": data})
    except requests.RequestException as e:
        logger.exception("External API request failed")
        return _err("Failed to fetch from external API.", 502, {"exception": str(e)})


# --- Main (local run only) ---
if __name__ == "__main__":
    # Local dev server (Render will use gunicorn)
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")))
