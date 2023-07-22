# Use Python as the base image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy Victim.py and HTML template files into the container
COPY Victim.py .
COPY templates templates

# Install Flask and its dependencies
RUN pip install --no-cache-dir Flask

# Expose port 5000, which is the default port for Flask applications
EXPOSE 5000

# Run the Flask application when the container starts
CMD ["python", "Victim.py"]

