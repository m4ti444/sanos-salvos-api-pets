# Sanos y Salvos - API Pets

API de gestion de mascotas y reportes de mascotas perdidas o encontradas.

## Stack

- FastAPI
- SQLAlchemy
- PostgreSQL/PostGIS
- RabbitMQ para eventos
- Docker

## Variables de entorno

Copia `.env.example` como `.env` y ajusta los valores.

## Ejecucion local

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8001
```

## Docker

```bash
docker build -t sanos-salvos-api-pets .
docker run --env-file .env -p 8001:8001 sanos-salvos-api-pets
```

## Endpoints principales

- `POST /api/pets/reports`
- `GET /api/pets/reports`
- `GET /api/pets/reports/{report_id}`
- `GET /api/pets/my-reports`
- `PATCH /api/pets/reports/{report_id}/status`
