# Changelog

## [Unreleased]
- Added `docker-compose.yml` to spin up Kafka, Zookeeper, DB, and backend in one command.
- Added unit tests for preprocessing and event producers.

## [2025-06-01] v1.0.0
- Initial release of Scalable Event-Driven Ride-Sharing Platform.
- Features:
  - Event producer/consumer modules using Kafka.
  - REST API for ride requests (FastAPI or Flask).
  - Basic data model and database schema for ride and driver tables.
  - Unit tests for core modules (data loading, preprocessing).
