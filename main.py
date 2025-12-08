import asyncio
from fastapi import FastAPI

from src.common.event_bus import EventBus
from src.common.utils import get_logger
from src.common.models import MatchResultEvent, DriverLocationEvent

from src.dispatch-service.producer import DispatchProducer
from src.dispatch-service.consumer import DispatchConsumer
from src.dispatch-service.api_router import router, DRIVER_STORE, MATCH_RESULTS_STORE

# --------------------------------------------------------------------
# CORE STATE STORES
# --------------------------------------------------------------------

# In-memory driver store populated by Driver Location Service
_driver_locations: list[DriverLocationEvent] = []

def driver_store():
    return list(_driver_locations)

# In-memory match results
_match_results: list[MatchResultEvent] = []

def match_results_store():
    return _match_results


# Surge lookup (injected later; stub for now)
def surge_lookup(zone_id: str) -> float:
    # In production → query pricing service cache
    return 1.0


# --------------------------------------------------------------------
# SERVICE INITIALIZATION
# --------------------------------------------------------------------

logger = get_logger("DispatchMain")
event_bus = EventBus()

app = FastAPI(
    title="Dispatch Service",
    description="Driver-rider matching microservice.",
    version="1.0.0",
)


# --------------------------------------------------------------------
# STARTUP SEQUENCE
# --------------------------------------------------------------------

@app.on_event("startup")
async def startup_event():

    logger.info("Starting Dispatch Service...")

    # Inject stores into API router
    global DRIVER_STORE, MATCH_RESULTS_STORE
    DRIVER_STORE = driver_store
    MATCH_RESULTS_STORE = _match_results

    # Initialize producer and consumer
    producer = DispatchProducer(event_bus)
    consumer = DispatchConsumer(
        event_bus=event_bus,
        driver_store=driver_store,
        surge_lookup=surge_lookup,
    )

    # Subscribe to trip requests
    await event_bus.subscribe("trip_requests", consumer.handle_trip_request)

    # Subscribe to match results
    async def match_result_listener(data):
        event = MatchResultEvent(**data)
        _match_results.append(event)
        logger.info(f"[DISPATCH] Stored match result for rider {event.rider_id}")

    await event_bus.subscribe("match_results", match_result_listener)

    # Start background async tasks
    asyncio.create_task(producer.start())

    logger.info("Dispatch Service started successfully.")


# --------------------------------------------------------------------
# ROUTER
# --------------------------------------------------------------------

app.include_router(router, prefix="/dispatch")


# --------------------------------------------------------------------
# LOCAL RUN
# --------------------------------------------------------------------

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "src.dispatch-service.main:app",
        host="0.0.0.0",
        port=8002,
        reload=True
    )
