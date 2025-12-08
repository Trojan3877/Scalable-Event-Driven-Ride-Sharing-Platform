import asyncio
import random
from src.common.utils import get_logger


class PricingProducer:
    """
    Publishes simulated supply/demand events for each zone.
    In production this could come from a real-time telemetry pipeline.
    """

    def __init__(self, event_bus):
        self.event_bus = event_bus
        self.logger = get_logger("PricingProducer")

    async def generate_supply_demand(self, zones=None):
        """
        Creates random (but realistic) demand and supply levels for testing.

        zones example: ["A1", "B2", "C3"]
        """

        if zones is None:
            zones = ["A1", "B2", "C3"]

        while True:
            zone_id = random.choice(zones)

            demand = random.randint(1, 40)   # number of riders requesting trips
            supply = random.randint(1, 25)   # number of available drivers

            event = {
                "zone_id": zone_id,
                "demand": demand,
                "supply": supply
            }

            await self.event_bus.publish("zone_supply_demand", event)

            self.logger.info(
                f"[PRODUCER] Published supply/demand event: {event}"
            )

            # control frequency of events
            await asyncio.sleep(1)

    async def start(self, zones=None):
        """
        Start the producer loop.
        """
        self.logger.info("PricingProducer started...")
        await self.generate_supply_demand(zones)
