from typing import Dict, List

from src.common.models import TripRequestEvent, DriverLocationEvent
from src.common.utils import get_logger
from src.dispatch-service.matching_engine import MatchingEngine


class DispatchConsumer:
    """
    Consumes TripRequestEvent messages, performs driver–rider matching,
    and publishes MatchResultEvent back to the event bus.

    This service interacts with:
    - Driver Location Service (driver store)
    - Pricing Service (surge multiplier)
    """

    def __init__(self, event_bus, driver_store, surge_lookup):
        """
        driver_store: callable -> returns List[DriverLocationEvent]
        surge_lookup: callable -> returns float
        """
        self.event_bus = event_bus
        self.driver_store = driver_store
        self.surge_lookup = surge_lookup
        self.engine = MatchingEngine()
        self.logger = get_logger("DispatchConsumer")

    # ------------------------------------------------------------
    # Core Handler
    # ------------------------------------------------------------

    async def handle_trip_request(self, data: Dict):
        """
        Expected TripRequestEvent:
        {
            "rider_id": "r123",
            "pickup_lat": 40.712,
            "pickup_lon": -74.005,
            "dropoff_lat": 40.730,
            "dropoff_lon": -73.935
        }
        """

        trip = TripRequestEvent(**data)

        self.logger.info(f"Received trip request from rider {trip.rider_id}")

        # ----------------------------
        # Load available drivers
        # ----------------------------
        available_drivers: List[DriverLocationEvent] = self.driver_store()

        if not available_drivers:
            self.logger.warning("No drivers available for matching.")
            return

        # ----------------------------
        # Get surge multiplier
        # ----------------------------
        zone_id = "default"  # later replaced with geospatial zone mapping
        surge_multiplier = self.surge_lookup(zone_id)

        # ----------------------------
        # Driver Matching
        # ----------------------------
        match_event = self.engine.select_best_match(
            drivers=available_drivers,
            trip=trip,
            surge_multiplier=surge_multiplier
        )

        if match_event is None:
            self.logger.warning("Failed to produce match event.")
            return

        # ----------------------------
        # Publish match result
        # ----------------------------
        await self.event_bus.publish("match_results", match_event.dict())

        self.logger.info(
            f"Published match result for rider {trip.rider_id} → driver {match_event.driver_id}"
        )

    # ------------------------------------------------------------
    # Subscription
    # ------------------------------------------------------------

    async def start(self):
        """
        Subscribe to incoming trip requests.
        """
        self.logger.info("DispatchConsumer subscribed to trip_request events...")
        await self.event_bus.subscribe("trip_requests", self.handle_trip_request)
