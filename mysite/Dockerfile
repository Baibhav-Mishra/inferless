# FROM python:3.8
FROM --platform=$BUILDPLATFORM python:3.8
EXPOSE 8000
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
# WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Install dependencies

# Copy the project code into the container
COPY . .

# RUN pip install -r requirements.txt
