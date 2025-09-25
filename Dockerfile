FROM ros:humble-ros-core AS autoware-guideline-check

RUN apt-get update && apt-get install -y \
    python3-pip \
    ros-humble-ament-index-python \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml LICENSE README.md /app/
COPY src /app/src/

RUN pip install --upgrade pip
RUN pip install /app
