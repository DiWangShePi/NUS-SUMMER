# Use Python as the base image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy Timing_Attack.py and requirements.txt into the container
COPY Timing_Attack.py .
COPY requirements.txt .

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the Timing_Attack.py script when the container starts
CMD ["python", "Timing_Attack.py"]

