FROM python:3.12-slim

# Copy and install dependencies
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

# Copy deployment script
COPY deployment.py /deployment.py

# Set the default command
CMD ["python", "/deployment.py"]
