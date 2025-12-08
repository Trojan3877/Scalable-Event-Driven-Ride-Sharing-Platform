# ============================================================
# Stage 1: Builder
# ============================================================
FROM python:3.10-slim AS builder

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy project code into image
COPY ../.. /app

# Install Python dependencies into wheels for caching
RUN pip install --upgrade pip
RUN pip wheel --no-cache-dir --wheel-dir /app/wheels -r requirements.txt



# ============================================================
# Stage 2: Final Runtime Image
# ============================================================
FROM python:3.10-slim

WORKDIR /app

# Create non-root user for security
RUN useradd -m appuser
USER appuser

# Copy built wheels and project source
COPY --from=builder /app/wheels /wheels
COPY --from=builder /app /app

# Install wheels
RUN pip install --no-cache /wheels/*

# Expose service port
EXPOSE 8002

# Kubernetes/Docker Healthcheck
HEALTHCHECK --interval=10s --timeout=3s \
  CMD curl -f http://localhost:8002/docs || exit 1

# Start Dispatch FastAPI service
CMD ["uvicorn", "src.dispatch-service.main:app", "--host", "0.0.0.0", "--port", "8002"]
