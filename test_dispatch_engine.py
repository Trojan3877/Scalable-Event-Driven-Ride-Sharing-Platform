import pytest

from src.dispatch-service.dispatch_engine import DispatchEngine


def test_dispatch_engine_selects_closest_driver():

    engine = DispatchEngine()

    drivers = [
        {"driver_id": "A", "latitude": 40.0, "longitude": -74.0},
        {"driver_id": "B", "latitude": 40.1, "longitude": -74.0},
        {"driver_id": "C", "latitude": 41.0, "longitude": -74.0},
    ]

    rider = {"latitude": 40.05, "longitude": -74.0}

    selected = engine.select_driver(drivers, rider)

    assert selected["driver_id"] == "A" or selected["driver_id"] == "B"
    # Both A and B are close; acceptable tie
