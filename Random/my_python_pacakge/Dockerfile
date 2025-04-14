FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies (in this case, only the local package)
RUN pip install .

# Command to run the Python script inside the container
CMD ["python", "-m", "my_python_package"]
