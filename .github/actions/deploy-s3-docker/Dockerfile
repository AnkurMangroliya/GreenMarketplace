FROM python:3

# Install dependencies
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# Copy deployment script
COPY deployment.py /deployment.py

# Set the default command to run the deployment script
CMD ["python", "/deployment.py"]
