# Use official Python slim image
FROM python:3.11-slim

# Install ffmpeg
RUN apt-get update && apt-get install -y ffmpeg && apt-get clean

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy code
COPY . .

# Expose Flask port
ENV PORT 8080

# Start with gunicorn
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8080"]
