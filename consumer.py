from src.pricing-service.pricing_engine import PricingEngine
from src.common.models import PricingEvent
from src.common.utils import get_logger


class PricingConsumer:
    """
    Consumes supply/demand events for each zone,
    computes surge multipliers, and publishes PricingEvents.
    """

    def __init__(self, event_bus):
        self.event_bus = event_bus
        self.engine = PricingEngine()
        self.logger = get_logger("PricingConsumer")

    async def handle_supply_demand(self, data: dict):
        """
        Example incoming event:
        {
            "zone_id": "A1",
            "demand": 15,
            "supply": 4
        }
        """
        zone_id = data["zone_id"]
        demand = data["demand"]
        supply = data["supply"]

        pricing_event: PricingEvent = self.engine.compute_surge(
            demand=demand,
            supply=supply,
            zone_id=zone_id
        )

        # Publish surge multiplier downstream
        await self.event_bus.publish("surge_updates", pricing_event.dict())

        self.logger.info(
            f"Published surge update for zone {zone_id}: {pricing_event.surge_multiplier}"
        )

    async def start(self):
        """
        Subscribe to supply/demand updates.
        """
        self.logger.info("PricingConsumer started. Listening for supply/demand events...")
        await self.event_bus.subscribe("zone_supply_demand", self.handle_supply_demand)
