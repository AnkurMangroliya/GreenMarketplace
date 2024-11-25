# Use the official Python image as the base image
FROM python:3.10-slim

# Workdir set
Workdir /app

# Copy code into workdir
Copy requirements.txt /app/

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && apt-get clean

# Install python dependencies.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django application code into the container
Copy . /app/

# Collect static file
RUN python manage.py collectstatic --noinput

# Expose the port the app runs on
EXPOSE 8000

# Command to run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]