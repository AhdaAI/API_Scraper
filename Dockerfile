FROM python:3.12-slim

# Set work directory
WORKDIR /usr/src/app

# Install system dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]