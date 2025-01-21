# Use the Python base image
FROM python:3.11.9-alpine3.20

# Set the working directory
WORKDIR /app/muddy-boots

# Install system dependencies
RUN apk update && apk add --no-cache \
    gcc \
    musl-dev \
    libffi-dev \
    openssl-dev \
    cmake \
    python3-dev \
    build-base \
    git \
    ninja \
    g++ \
    make

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the default command
CMD ["python"]
