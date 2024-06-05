FROM --platform=$BUILDPLATFORM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /mysite
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project code into the container
COPY . .

