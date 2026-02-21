FROM python:3.11-slim

WORKDIR /app

COPY ../../shared ./shared
COPY ./main.py .

RUN pip install --no-cache-dir fastapi uvicorn kafka-python \
    python-json-logger pydantic redis psycopg2-binary prometheus-client

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]