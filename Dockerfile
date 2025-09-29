FROM ubuntu:22.04 AS autoware-guideline-check

RUN apt-get update && apt-get install -y \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /autoware_guideline_check
COPY pyproject.toml LICENSE README.md /autoware_guideline_check/
COPY src /autoware_guideline_check/src/

RUN pip install --upgrade pip
RUN pip install /autoware_guideline_check

ENTRYPOINT ["autoware-guideline-check"]
