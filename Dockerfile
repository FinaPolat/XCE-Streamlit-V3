# Base image: Use official Python slim version
FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app

# Install necessary packages
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

# Copy all files from the current directory to /app in the container
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Expose port 8501 for Streamlit
EXPOSE 8501

# Healthcheck to verify if the service is running
HEALTHCHECK CMD curl --fail http://localhost:8501/ || exit 1

# Define the command to run the Streamlit app
ENTRYPOINT ["streamlit", "run", "streamlit_app_v3.py", "--server.port=8501", "--server.address=0.0.0.0"]
