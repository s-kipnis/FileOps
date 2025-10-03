from __future__ import annotations

import uvicorn


def main() -> None:
    """
    Local server entrypoint:
      - host: 127.0.0.1
      - port: 8000
    """
    uvicorn.run(
        "file_ops.app:app",
        host="127.0.0.1",
        port=8000,
        reload=False,  # set True for dev auto-reload if needed
        log_level="info",
    )


if __name__ == "__main__":
    main()
