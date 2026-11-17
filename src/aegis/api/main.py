"""FastAPI app. Week 0 only needs /health so `docker compose up` can be checked."""
from fastapi import FastAPI

app = FastAPI(title="Aegis")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
