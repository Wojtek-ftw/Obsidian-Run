# Use the official Jupyter image with Python
FROM jupyter/scipy-notebook:latest

# Optional: set a working directory
WORKDIR /home/jovyan/work
COPY . /home/jovyan/work


# Copy your custom package into the container
COPY numpy_analysis /home/jovyan/work/numpy_analysis


# Install additional Python packages
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install .


# Expose Jupyter port (default is 8888)
EXPOSE 8888
