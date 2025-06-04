# Use a slim Python base image
FROM python:3.9-slim

# Set a working directory
WORKDIR /app

# Copy only requirements first (for better caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .

# Expose any ports (e.g., if you have an API service on 8000)
EXPOSE 8000

# Default entrypoint (for example, start your main service)
ENTRYPOINT ["bash", "run_pipeline.sh"]
