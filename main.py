import asyncio
import os

from src.event-bus.kafka_bus import KafkaEventBus
from src.event-bus.redis_bus import RedisEventBus
from src.event-bus.rabbitmq_bus import RabbitMQEventBus

from src.matching-service.consumer import MatchingConsumer
from src.common.utils import get_logger


def get_event_bus():
    backend = os.getenv("EVENT_BUS_BACKEND", "kafka").lower()

    if backend == "kafka":
        return KafkaEventBus()
    elif backend == "redis":
        return RedisEventBus()
    elif backend == "rabbitmq":
        return RabbitMQEventBus()
    else:
        raise ValueError(f"Unsupported EVENT_BUS_BACKEND: {backend}")


async def main():
    logger = get_logger("MatchingService")

    event_bus = get_event_bus()

    logger.info(f"Using event bus backend: {event_bus.__class__.__name__}")

    # Connect to Kafka / Redis / RabbitMQ
    await event_bus.connect()

    consumer = MatchingConsumer(event_bus)

    try:
        logger.info("Starting Matching Service...")
        await consumer.start()
    except Exception as e:
        logger.error(f"Fatal error in Matching Service: {e}")
    finally:
        logger.info("Shutting down Matching Service...")
        await event_bus.close()


if __name__ == "__main__":
    asyncio.run(main())
