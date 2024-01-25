dev:
	@SSL_CERT_FILE=./certs/cert.pem SSL_KEY_FILE=./certs/key.pem app.py

start:
	@app.py

lint:
	@ruff check --config=.ruff.toml app/*

.PHONY: dev start lint