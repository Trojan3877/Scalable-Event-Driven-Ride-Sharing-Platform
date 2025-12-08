from fastapi import APIRouter, HTTPException
from src.pricing-service.pricing_engine import PricingEngine
from src.common.utils import get_logger

router = APIRouter()
logger = get_logger("PricingAPI")

# In-memory surge cache for fast lookup
SURGE_CACHE = {}  # { "A1": 1.8, "B2": 1.2, ... }

def update_surge(zone_id: str, multiplier: float):
    """
    Called by the consumer after computing new zone surge.
    """
    SURGE_CACHE[zone_id] = multiplier
    logger.info(f"[API] Updated surge multiplier for zone {zone_id} = {multiplier}")


@router.get("/surge/{zone_id}")
async def get_surge(zone_id: str):
    """
    Fetch latest surge multiplier for a given zone.
    """
    if zone_id not in SURGE_CACHE:
        raise HTTPException(
            status_code=404,
            detail=f"No surge information available for zone {zone_id}"
        )

    return {
        "zone_id": zone_id,
        "surge_multiplier": SURGE_CACHE[zone_id]
    }


@router.get("/surge/all")
async def get_all_surge():
    """
    Get all current surge multipliers for every zone.
    """
    return SURGE_CACHE
