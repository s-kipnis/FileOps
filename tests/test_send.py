from __future__ import annotations

from fastapi.testclient import TestClient

from file_ops.app import app

client = TestClient(app)


def test_health() -> None:
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}


def test_send_json() -> None:
    payload = {"message": "hi", "meta": {"k": 1}}
    resp = client.post("/send", json=payload)
    assert resp.status_code == 200
    body = resp.json()
    assert body["ok"] is True
    assert body["echo"]["message"] == "hi"
    assert body["echo"]["meta"] == {"k": 1}


def test_send_text() -> None:
    resp = client.post("/send", data="hello", headers={"content-type": "text/plain"})
    assert resp.status_code == 200
    body = resp.json()
    assert body["ok"] is True
    assert body["echo"]["message"] == "hello"
