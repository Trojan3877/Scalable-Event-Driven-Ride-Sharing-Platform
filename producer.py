from src.common.models import RideRequest, DriverLocation
from src.common.utils import get_logger


class MatchingProducer:
    """
    Utility class for publishing ride requests and driver updates
    into the event-driven system.
    Used for testing, load generation, or manual event injection.
    """

    def __init__(self, event_bus):
        self.event_bus = event_bus
        self.logger = get_logger("MatchingProducer")

    async def publish_ride_request(self, request: RideRequest):
        self.logger.info(
            f"Publishing ride request {request.request_id} for passenger {request.passenger_id}"
        )
        await self.event_bus.publish("ride_requests", request.dict())

    async def publish_driver_update(self, driver: DriverLocation):
        self.logger.info(
            f"Publishing driver update for driver {driver.driver_id}"
        )
        await self.event_bus.publish("driver_updates", driver.dict())
