from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version="1.0.0",
    description="API de Ingestión de Datos - Versión de demostración."
)

@app.get("/health")
def health_check():
    """
    Endpoint básico de salud para operaciones MLOps / DevOps.
    """
    return {"status": "healthy", "version": "1.0.0"}

# Aquí iría el app.include_router(ingest_api.router)
