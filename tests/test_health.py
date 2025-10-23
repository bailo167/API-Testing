import json
from app import app

def test_healthz():
    client = app.test_client()
    res = client.get("/healthz")
    assert res.status_code == 200
    data = json.loads(res.data)
    assert data["ok"] is True
    assert "status" in data["data"]
