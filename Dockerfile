# Use official Python slim image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY req.txt .

RUN pip install --no-cache-dir -r req.txt

# Copy the rest of the application code
COPY . .

EXPOSE 8010

# Run the application with uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8010"]
