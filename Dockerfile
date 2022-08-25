#Tells Docker to use the official python 3 image from dockerhub as a base image
FROM python:3.10-slim as builder

# Sets the container's working directory to /app
WORKDIR /app

# Sets an environmental variable that ensures output from python is sent straigetss192etssht to the terminal without buffering it first
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc

# Copies all files from our local project into the container
COPY . .

RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt

# Final Stage
FROM python:3.10-slim-bullseye

WORKDIR /app


COPY --from=builder /app/wheels /wheels
COPY --from=builder /app/requirements.txt .

RUN pip install --no-cache /wheels/*