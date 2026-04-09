FROM python:3.10

# Set working directory
WORKDIR /app

# Copy all files
COPY . .

# Install dependencies with timeout fix
RUN pip install --no-cache-dir --default-timeout=100 flask

# Run application
CMD ["python", "app.py"]