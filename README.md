# Enterprise Data Ingestion & Cleaning Engine (Portfolio Demo)

> **Aviso Importante:** Este repositorio es una demostración arquitectónica ("hollow code" o código esqueleto) creada para mi portafolio. Toda la propiedad intelectual, lógica de negocio privada, modelos de datos específicos y credenciales de la empresa *Dataset* han sido removidos u ofuscados. 

Este proyecto demuestra mi experiencia en la construcción de sistemas backend escalables, específicamente en la refactorización y creación de pipelines de ingestión de datos a nivel empresarial.

## 🚀 El Problema que Resolví
El sistema legado de ingestión procesaba archivos grandes de manera monolítica (cargando todo en memoria). Esto provocaba cuellos de botella severos ("worker time-limit errors") cuando los clientes subían matrices o archivos Excel/CSV de más de 2GB. Además, la falta de validación temprana permitía corrupciones en la codificación de caracteres.

## 💡 Mi Contribución y Solución Técnica
Lideré la refactorización arquitectónica para migrar hacia un pipeline asíncrono y resiliente, destacando:
1. **Validación Temprana (Fase 1):** Implementé un motor de inspección de `Magic Bytes` para validar el formato real de los archivos independientemente de su extensión, previniendo fallos en memoria causados por archivos corruptos o maliciosos.
2. **Procesamiento por Chunks:** Diseñé un motor de ingestión que convierte grandes cargas a formato `Parquet` y las procesa en fragmentos (chunks) usando Pandas y PyArrow, reduciendo el consumo de RAM en un 80% y eliminando los timeouts.
3. **Normalización y Limpieza:** Creé un motor (`cleaning/engine_v1.py`) con "Global Native Rescue" para manejar de manera robusta los BOM, encodings anómalos y heurísticas para matrices "sucias".

## 🛠️ Stack Tecnológico
*   **Lenguaje:** Python 3.10+
*   **Framework:** FastAPI
*   **Data Processing:** Pandas, PyArrow (Parquet)
*   **Arquitectura:** DDD (Domain-Driven Design), Clean Architecture principles
*   **Despliegue:** Docker, Docker Compose

## 📁 Arquitectura del Repositorio (Demostración)

La estructura a continuación muestra mi estilo de diseño modular:

```text
backend/
├── app/
│   ├── api/             # Endpoints y Controladores (FastAPI)
│   ├── core/            # Configuración base, BaseSettings, Seguridad
│   ├── models/          # Modelos Pydantic y Entidades ORM
│   ├── services/
│   │   ├── cleaning/    # Motores de Limpieza (Normalización, Imputación)
│   │   └── ingestion/   # Recepción, Validación de Magic Bytes, Formateo
│   └── main.py          # Entrypoint de la aplicación
```

Puedes inspeccionar los archivos dentro de `backend/app/services` para ver mi manejo de **Type Hints**, diseño de clases, manejo de excepciones y documentación técnica integrada.
