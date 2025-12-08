import asyncio
from fastapi import FastAPI

from src.common.event_bus import EventBus
from src.common.utils import get_logger
from src.common.models import DriverLocationEvent

from src.driver-location-service.location_store import DriverLocationStore
from src.driver-location-service.consumer import DriverLocationConsumer
from src.driver-location-service.api_router import router, DRIVER_STORE


# ------------------------------------------------------------
# INITIALIZATION
# ------------------------------------------------------------

logger = get_logger("DriverLocationMain")

event_bus = EventBus()
driver_store = DriverLocationStore()

app = FastAPI(
    title="Driver Location Service",
    description="Real-time driver location ingestion service for the ride-sharing platform.",
    version="1.0.0",
)


# ------------------------------------------------------------
# STARTUP SEQUENCE
# ------------------------------------------------------------

@app.on_event("startup")
async def startup_event():

    logger.info("Starting Driver Location Service...")

    # Inject store into API router
    global DRIVER_STORE
    DRIVER_STORE = driver_store

    # Initialize consumer
    consumer = DriverLocationConsumer(
        event_bus=event_bus,
        store=driver_store
    )

    # Subscribe to driver location update events
    await event_bus.subscribe(
        "driver_location_updates",
        consumer.handle_driver_location
    )

    logger.info("Driver Location Service started successfully.")


# ------------------------------------------------------------
# ROUTER
# ------------------------------------------------------------

app.include_router(router, prefix="/driver-location")


# ------------------------------------------------------------
# LOCAL RUNNER
# ------------------------------------------------------------

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "src.driver-location-service.main:app",
        host="0.0.0.0",
        port=8003,
        reload=True
    )
