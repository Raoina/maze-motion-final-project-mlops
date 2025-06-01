# Use tiangolo image that already has FastAPI, Uvicorn, Gunicorn setup
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10-slim

# Set the working directory
WORKDIR /app

# Copy requirements and install
COPY req.txt .

RUN pip install --no-cache-dir -r req.txt

# Copy the application code
COPY . .

ENV MODULE_NAME=app.main

