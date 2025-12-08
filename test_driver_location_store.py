import pytest
from src.driver-location-service.location_store import DriverLocationStore
from src.common.models import DriverLocationEvent


def test_driver_location_store_updates_and_retrieves():

    store = DriverLocationStore()

    event = DriverLocationEvent(
        driver_id="d1",
        latitude=40.7128,
        longitude=-74.0060,
        accuracy=3.5,
        timestamp=1234567890
    )

    store.update_location(event)
    results = store.get_nearby_drivers(40.7128, -74.0060, radius_km=5)

    assert len(results) == 1
    assert results[0]["driver_id"] == "d1"
