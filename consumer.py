import asyncio
from src.common.models import RideRequest, DriverLocation
from src.common.utils import get_logger
from src.matching-service.matching_engine import MatchingEngine


class MatchingConsumer:
    """
    Consumes ride-request and driver-location events from the EventBus,
    feeds them into MatchingEngine, and triggers match generation.
    """

    def __init__(self, event_bus):
        self.event_bus = event_bus
        self.engine = MatchingEngine()
        self.logger = get_logger("MatchingConsumer")

    async def handle_ride_request(self, data: dict):
        request = RideRequest(**data)
        self.logger.info(f"Received ride request {request.request_id}")

        match_result = self.engine.find_best_driver(request)

        if match_result:
            self.logger.info(
                f"Matched request {request.request_id} "
                f"with driver {match_result.driver_id}"
            )
            # Publish match result to event bus
            await self.event_bus.publish("match_results", match_result.dict())
        else:
            self.logger.warning(
                f"No drivers available for request {request.request_id}"
            )

    async def handle_driver_update(self, data: dict):
        driver = DriverLocation(**data)
        self.logger.info(f"Updated driver {driver.driver_id} location")
        self.engine.update_driver_location(driver)

    async def start(self):
        """
        Subscribes to ride request + driver updates.
        Two streams:
        - ride_requests
        - driver_updates
        """

        self.logger.info("MatchingConsumer started. Subscribing to topics...")

        await asyncio.gather(
            self.event_bus.subscribe(
                "ride_requests", self.handle_ride_request
            ),
            self.event_bus.subscribe(
                "driver_updates", self.handle_driver_update
            ),
        )
