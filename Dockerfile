# Use official Python slim image
FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements file and install dependencies
COPY req.txt .

RUN pip install --no-cache-dir -r req.txt

# Copy the rest of the application code
COPY . .

# Expose port (FastAPI default 8000)
EXPOSE 8000

# Command to run the app with uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
