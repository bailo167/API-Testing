# API Testing (Flask on Render)

A minimal Flask API + static frontend, deployable on Render. Includes CORS, healthcheck, example external API call, and simple tests.

## Endpoints
- `GET /` — serves `static/index.html`
- `GET /healthz` — service health
- `GET /api/ping` — returns `"pong"`
- `GET /api/calc?a=5&b=7` — demo query params
- `POST /api/echo` — echoes JSON body
- `GET /api/external` — calls `THIRD_PARTY_API_URL` with optional `EXTERNAL_API_KEY`

## Local Development
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # optional for local values
export FLASK_ENV=development
python app.py
# visit http://127.0.0.1:5000
