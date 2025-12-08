from pydantic import BaseModel, Field
from typing import Optional
from uuid import uuid4
from datetime import datetime


def generate_id():
    return str(uuid4())


class RideRequest(BaseModel):
    request_id: str = Field(default_factory=generate_id)
    passenger_id: str
    pickup_lat: float
    pickup_lng: float
    dropoff_lat: float
    dropoff_lng: float
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    surge_multiplier: Optional[float] = 1.0


class DriverLocation(BaseModel):
    driver_id: str
    lat: float
    lng: float
    is_available: bool = True
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class MatchResult(BaseModel):
    match_id: str = Field(default_factory=generate_id)
    request_id: str
    driver_id: str
    eta_minutes: float
    distance_km: float
    surge_multiplier: float
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class PricingEvent(BaseModel):
    zone_id: str
    demand: int
    supply: int
    surge_multiplier: float
    timestamp: datetime = Field(default_factory=datetime.utcnow)
