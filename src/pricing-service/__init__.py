"""
Driver Location Service Package

This package handles real-time ingestion, storage,
and retrieval of driver GPS coordinates for the
Scalable Event-Driven Ride-Sharing Platform.
"""

from .location_store import DriverLocationStore
from .consumer import DriverLocationConsumer
