"""
Dispatch Service Package

Includes:
- matching_engine.py  → Core driver–rider matching logic
- consumer.py         → TripRequestEvent consumer
- producer.py         → Trip request generator for testing
- api_router.py       → FastAPI router for monitoring and debugging
- main.py             → Full microservice runtime entrypoint

This service listens for:
- trip_requests
- match_results

And produces:
- MatchResultEvent (driver → rider assignment)
"""
