# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Clone the GitHub repository into the container
RUN git clone https://github.com/arinaleech/vgcghc.git /app

# Update package list and install required system dependencies
RUN apt-get update && \
    apt-get install -y ffmpeg aria2 git wget pv jq python3-dev mediainfo && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Python dependencies from requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Force reinstall brotli if needed
RUN pip install --force-reinstall brotli

# Install and upgrade yt-dlp
RUN pip uninstall -y yt-dlp && \
    pip install yt-dlp && \
    pip install --upgrade yt-dlp

# Verify ffmpeg and yt-dlp installation
RUN ffmpeg -version
RUN yt-dlp --version

# Set the working directory to where the code was cloned
WORKDIR /app

# Expose the port if needed (this is optional depending on your app)
# EXPOSE 8080

# Run the application (assuming the entry file is bot.py)
CMD ["python3", "bot.py"]
