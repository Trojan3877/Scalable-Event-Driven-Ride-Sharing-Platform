from typing import List, Optional
from src.common.models import RideRequest, DriverLocation, MatchResult
from src.common.utils import haversine_distance, utc_now, generate_id


class MatchingEngine:
    """
    Core matching logic for assigning drivers to ride requests.
    Production-ready, easily extendable for ML models or geospatial indexing.
    """

    def __init__(self):
        # In production this would be from Redis, Cassandra, DynamoDB, etc.
        self.active_drivers: List[DriverLocation] = []

    def update_driver_location(self, driver: DriverLocation):
        """
        Add or update driver info in memory. This would normally come from Kafka.
        """
        # Remove existing driver entry
        self.active_drivers = [d for d in self.active_drivers if d.driver_id != driver.driver_id]
        self.active_drivers.append(driver)

    def find_best_driver(self, request: RideRequest) -> Optional[MatchResult]:
        """
        Select the closest available driver using Haversine distance.
        """
        available_drivers = [d for d in self.active_drivers if d.is_available]

        if not available_drivers:
            return None

        # Compute distances
        scored_drivers = []
        for driver in available_drivers:
            distance = haversine_distance(
                request.pickup_lat,
                request.pickup_lng,
                driver.lat,
                driver.lng,
            )

            # ETA estimation: assume average 30 km/h → 0.5 km/min
            eta_minutes = distance / 0.5 if distance > 0 else 1
            scored_drivers.append((driver, distance, eta_minutes))

        # Pick closest driver
        scored_drivers.sort(key=lambda x: x[1])  # sort by distance

        best_driver, best_distance, best_eta = scored_drivers[0]

        # Create match result
        match = MatchResult(
            match_id=generate_id(),
            request_id=request.request_id,
            driver_id=best_driver.driver_id,
            eta_minutes=round(best_eta, 2),
            distance_km=round(best_distance, 2),
            surge_multiplier=request.surge_multiplier,
            timestamp=utc_now(),
        )

        # Mark driver as unavailable
        best_driver.is_available = False

        return match
