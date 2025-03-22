# Use Ubuntu as the base image
FROM ubuntu:latest

# Set environment variables to ensure non-interactive installation
ENV DEBIAN_FRONTEND=noninteractive

# Update the package list and install Python3, pip, and dependencies
RUN apt-get update -y && apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \
    python3-setuptools \
    python3-venv \
    && apt-get clean

# Create a Python virtual environment
RUN python3 -m venv /home/doc-bd-a1/venv

# Upgrade pip inside the virtual environment and install required Python packages
RUN /home/doc-bd-a1/venv/bin/pip install --upgrade pip && \
    /home/doc-bd-a1/venv/bin/pip install pandas numpy seaborn matplotlib scikit-learn scipy

# Set the working directory inside the container
WORKDIR /home/doc-bd-a1

# Set the default command to start bash and activate the virtual environment
CMD ["bash", "-c", "source /home/doc-bd-a1/venv/bin/activate && exec bash"]
