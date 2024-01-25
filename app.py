#!/usr/bin/env python3

import os

import uvicorn

from app.main import bootstrap


def main():
    uvicorn.run(
        app=bootstrap,
        factory=True,
        host=os.getenv("HOST", "127.0.0.1"),
        port=int(os.getenv("PORT", "3000")),
        ssl_certfile=os.getenv("SSL_CERT_FILE"),
        ssl_keyfile=os.getenv("SSL_KEY_FILE"),
        server_header=False,
        date_header=False,
        log_config=None,
    )


if __name__ == "__main__":
    main()
