from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """
    Gestión de configuración utilizando Pydantic para validar variables de entorno.
    (Las contraseñas o URIs reales se inyectan en CI/CD, nunca en el repositorio)
    """
    PROJECT_NAME: str = "Enterprise Ingestion Pipeline"
    API_V1_STR: str = "/api/v1"
    
    # Configuraciones de chunking para evitar Timeouts
    MAX_FILE_SIZE_MB: int = 5000
    CHUNK_SIZE_ROWS: int = 50000

    class Config:
        env_file = ".env"

settings = Settings()
