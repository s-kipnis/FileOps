from __future__ import annotations

from typing import Any

from fastapi import FastAPI, Request, Response
from pydantic import BaseModel

app = FastAPI(title="file_ops", version="0.1.1")


class SendModel(BaseModel):
    # Accepts {"message": "...", "meta": {...}}; "meta" is optional
    message: str
    meta: dict[str, Any] | None = None


@app.get("/health")
async def health() -> dict[str, str]:
    # Simple liveness check
    return {"status": "ok"}


@app.post("/blob")
async def blob(request: Request) -> Response:
    """
    Accepts large binary data (up to ~100 MB).
    Reads request body in streaming chunks for efficiency.
    Echoes back processed (or identical) binary data.
    """
    # Read binary data in chunks
    # (streaming avoids loading full 100MB into memory at once)
    chunks = []
    async for chunk in request.stream():
        chunks.append(chunk)
    data = b"".join(chunks)

    # Example: process or modify binary data
    # (you can replace this with real logic)
    processed = data  # here we just echo it

    # Return binary response
    return Response(content=processed, media_type="application/octet-stream")


@app.post("/send")
async def send(request: Request) -> dict[str, Any]:
    """
    Accepts application/json -> validated by SendModel.
    If content-type is text/plain (or other), read raw body as text.
    Returns an echo payload in a unified JSON structure.
    """
    content_type = request.headers.get("content-type", "")

    if "application/json" in content_type:
        data = await request.json()
        # Validate into SendModel (handles both dict and bare value fallback)
        if isinstance(data, dict):
            model = SendModel.model_validate(data)
            return {"ok": True, "echo": model.model_dump()}
        # Fallback for non-dict JSON (e.g., a string/number/array)
        model = SendModel(message=str(data))
        return {"ok": True, "echo": model.model_dump()}

    # text/plain or any other content-type: treat as raw text
    raw = await request.body()
    model = SendModel(message=raw.decode("utf-8"))
    return {"ok": True, "echo": model.model_dump()}
