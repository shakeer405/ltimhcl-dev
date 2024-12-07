# Use the official Python image
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy application files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the application with Gunicorn
CMD exec gunicorn -b :$PORT main:app

