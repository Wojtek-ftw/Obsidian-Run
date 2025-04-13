# Use the official Jupyter image with Python
FROM jupyter/scipy-notebook:latest

# Optional: set a working directory
WORKDIR /home/johndoe/work

# Copy your custom package into the container
COPY numpy_analysis /home/johndoe/work/numpy_analysis

COPY requirements.txt ./
COPY numpy_analysis ./numpy_analysis

# Install additional Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose Jupyter port (default is 8888)
EXPOSE 8888
