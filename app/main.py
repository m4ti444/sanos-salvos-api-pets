"""
Sanos y Salvos — Pets Microservice
Manages structured pet reports (lost & found).
"""

import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy import text

from app.api.routes import router
from app.config import Base, engine
from app.models import pet, report
from app.events.publisher import publisher

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("pets-service")

def init_database():
    """Create service schema and tables when running in a fresh database."""
    with engine.begin() as conn:
        conn.execute(text("CREATE SCHEMA IF NOT EXISTS pets_service"))
    Base.metadata.create_all(bind=engine)



@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("🐾 Pets Microservice starting...")
    await publisher.connect()
    yield
    await publisher.close()
    logger.info("🛑 Pets Microservice shutting down...")


app = FastAPI(
    title="Sanos y Salvos — Gestión de Mascotas",
    description="Microservicio para registro y gestión de reportes de mascotas perdidas y encontradas",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.get("/health")
def health():
    return {"status": "healthy", "service": "pets-service"}
