from __future__ import annotations

import io
import os

import pytest
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
    resp = client.post("/send", content=b"hello", headers={"content-type": "text/plain"})
    assert resp.status_code == 200
    body = resp.json()
    assert body["ok"] is True
    assert body["echo"]["message"] == "hello"


@pytest.mark.parametrize("size_mb", [0, 1, 5])  # test empty, 1MB, 5MB
def test_blob_echo(size_mb: int) -> None:
    """
    Tests that /blob correctly echoes binary data of various sizes.
    """
    # Generate binary data
    size_bytes = size_mb * 1024 * 1024
    data = os.urandom(size_bytes)

    # Send binary data to the endpoint
    response = client.post(
        "/blob",
        content=io.BytesIO(data),
        headers={"Content-Type": "application/octet-stream"},
    )

    # Verify response
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/octet-stream"
    assert response.content == data


def test_blob_partial_match() -> None:
    """
    Test partial data comparison to ensure binary integrity check works.
    """
    data = b"1234567890ABCDEF"
    response = client.post(
        "/blob", content=data, headers={"Content-Type": "application/octet-stream"}
    )
    assert response.status_code == 200
    assert response.content[:5] == data[:5]
    assert len(response.content) == len(data)


def test_blob_invalid_content_type() -> None:
    """
    Sending incorrect content type should still be accepted as raw bytes.
    """
    data = b"hello world"
    response = client.post("/blob", content=data, headers={"Content-Type": "text/plain"})
    assert response.status_code == 200
    assert response.content == data
