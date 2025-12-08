# ============================================================
# Stage 1: Builder
# ============================================================
FROM python:3.10-slim AS builder

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY ../.. /app

# Install Python dependencies into a wheel folder
RUN pip install --upgrade pip
RUN pip wheel --no-cache-dir --wheel-dir /app/wheels -r requirements.txt



# ============================================================
# Stage 2: Final Runtime Image
# ============================================================
FROM python:3.10-slim

WORKDIR /app

# Add a non-root system user for security
RUN useradd -m appuser
USER appuser

# Copy wheels built in stage 1
COPY --from=builder /app/wheels /wheels
COPY --from=builder /app /app
RUN pip install --no-cache /wheels/*

# Expose service port
EXPOSE 8003

# Healthcheck for container orchestration
HEALTHCHECK --interval=10s --timeout=3s \
  CMD curl -f http://localhost:8003/docs || exit 1

# Start FastAPI service
CMD ["uvicorn", "src.driver-location-service.main:app", "--host", "0.0.0.0", "--port", "8003"]
