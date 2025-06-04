#!/usr/bin/env bash
set -e

echo "🔄 [run_pipeline] Starting end-to-end pipeline"

# 1. Build local artifacts (if any)
echo "📦 Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# 2. Create topics or initialize event broker if needed
#   (e.g., python scripts to create Kafka topics)
python src/setup_kafka_topics.py

# 3. Start producers / consumers for ride requests
echo "⚙️  Launching backend services..."
# Example: run the main service (adjust the command to your entrypoint)
python src/main.py --config config/dev.yaml

# 4. Optionally run tests or health checks
echo "✅ Pipeline is running. Press Ctrl+C to stop."
