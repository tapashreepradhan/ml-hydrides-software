FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /workspace

# Copy the requirements file into the container at /workspace
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the working directory contents into the container at /workspace
COPY . .
