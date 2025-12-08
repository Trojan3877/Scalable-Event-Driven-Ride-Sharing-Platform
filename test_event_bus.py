import asyncio
import pytest

from src.common.event_bus import EventBus


@pytest.mark.asyncio
async def test_event_bus_publish_and_subscribe():

    bus = EventBus()
    received_messages = []

    async def handler(payload):
        received_messages.append(payload)

    # Subscribe
    await bus.subscribe("test_topic", handler)

    # Publish event
    await bus.publish("test_topic", {"value": 123})

    # Allow async loop to process event
    await asyncio.sleep(0.1)

    assert len(received_messages) == 1
    assert received_messages[0]["value"] == 123
