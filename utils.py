import json
import logging
import math
from datetime import datetime
from uuid import uuid4


# ----------------------------
# Logging Configuration
# ----------------------------

def get_logger(service_name: str):
    """
    Creates a consistent logger for all microservices.
    """
    logger = logging.getLogger(service_name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger


# ----------------------------
# Distance Calculation (Haversine)
# ----------------------------

def haversine_distance(lat1, lon1, lat2, lon2):
    """
    Calculates the distance between two GPS coordinates in kilometers.
    """
    R = 6371  # Earth radius in km

    d_lat = math.radians(lat2 - lat1)
    d_lon = math.radians(lon2 - lon1)

    a = (
        math.sin(d_lat / 2) ** 2
        + math.cos(math.radians(lat1))
        * math.cos(math.radians(lat2))
        * math.sin(d_lon / 2) ** 2
    )
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c


# ----------------------------
# Time Utilities
# ----------------------------

def utc_now():
    return datetime.utcnow()


# ----------------------------
# JSON Serialization Helpers
# ----------------------------

def to_json(data):
    return json.dumps(data, default=str)


def from_json(json_str):
    return json.loads(json_str)


# ----------------------------
# ID Generators
# ----------------------------

def generate_id():
    return str(uuid4())
