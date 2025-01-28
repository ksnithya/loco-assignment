# Stage 1: Build
FROM python:3.11-slim as builder

# Set the working directory
WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt --target /app/dependencies

# Stage 2: Runtime
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy application source code
COPY app.py .

# Copy installed dependencies from the builder stage
COPY --from=builder /app/dependencies /app/dependencies

# Set the Python path to include the dependencies
ENV PYTHONPATH=/app/dependencies

# Expose the application port
EXPOSE 80

ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
