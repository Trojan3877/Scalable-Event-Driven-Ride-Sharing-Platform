from fastapi import APIRouter, HTTPException
from typing import List, Dict

from src.common.models import DriverLocationEvent, MatchResultEvent
from src.common.utils import get_logger

router = APIRouter()
logger = get_logger("DispatchAPI")


# These will be injected by main.py
DRIVER_STORE = None          # Callable → List[DriverLocationEvent]
MATCH_RESULTS_STORE = None   # List[MatchResultEvent]


@router.get("/drivers")
async def get_available_drivers():
    """
    Returns the list of currently available drivers.
    """
    if DRIVER_STORE is None:
        raise HTTPException(status_code=500, detail="Driver store not initialized.")

    drivers = DRIVER_STORE()
    return {"count": len(drivers), "drivers": drivers}


@router.get("/matches")
async def get_match_results():
    """
    Returns a list of recent match results.
    """
    if MATCH_RESULTS_STORE is None:
        raise HTTPException(status_code=500, detail="Match results store not initialized.")

    return {"count": len(MATCH_RESULTS_STORE), "matches": MATCH_RESULTS_STORE}


@router.get("/matches/{index}")
async def get_match_by_index(index: int):
    """
    Fetch a specific match result by list index.
    """
    if MATCH_RESULTS_STORE is None or index < 0 or index >= len(MATCH_RESULTS_STORE):
        raise HTTPException(status_code=404, detail="Match not found.")

    return MATCH_RESULTS_STORE[index]


@router.get("/health")
async def health_check():
    """
    Service status check.
    """
    return {"status": "OK", "service": "dispatch-service"}
