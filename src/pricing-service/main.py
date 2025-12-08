import asyncio
from fastapi import FastAPI

from src.common.event_bus import EventBus
from src.common.utils import get_logger

from src.pricing-service.api_router import router, update_surge, SURGE_CACHE
from src.pricing-service.consumer import PricingConsumer
from src.pricing-service.producer import PricingProducer
from src.pricing-service.pricing_engine import PricingEngine

logger = get_logger("PricingServiceMain")


app = FastAPI(
    title="Pricing Service",
    description="Real-time surge pricing engine for ride-sharing platform.",
    version="1.0.0",
)


# ----------------------------
# Initialize core components
# ----------------------------
event_bus = EventBus()
producer = PricingProducer(event_bus)
consumer = PricingConsumer(event_bus)
engine = PricingEngine()


# ----------------------------
# Startup Sequence
# ----------------------------

@app.on_event("startup")
async def startup_event():

    logger.info("Starting Pricing Service...")

    # Subscribe consumer to supply/demand topic
    await event_bus.subscribe(
        topic="zone_supply_demand",
        callback=consumer.handle_supply_demand
    )

    # Launch producer + consumer loop
    asyncio.create_task(producer.start())

    logger.info("Pricing Service started successfully.")


# ----------------------------
# API Router
# ----------------------------
app.include_router(router, prefix="/pricing")


# ----------------------------
# Health Check Endpoint
# ----------------------------

@app.get("/health")
async def health_check():
    return {
        "status": "OK",
        "service": "pricing-service",
        "surge_cache_size": len(SURGE_CACHE),
    }


# ----------------------------
# Manual run for local usage
# ----------------------------
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "src.pricing-service.main:app",
        host="0.0.0.0",
        port=8001,
        reload=True
    )
