#Tells Docker to use the official python 3 image from dockerhub as a base image
FROM python:3.8-slim as builder

# Sets the container's working directory to /app
WORKDIR /app

# Sets an environmental variable that ensures output from python is sent straight to the terminal without buffering it first
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc apt default-libmysqlclient-dev

# Copies all files from our local project into the container
COPY . .

RUN python -m pip install --upgrade pip
RUN python -m pip install virtualenv
RUN pip install -r requirements.txt

# Final Stage
FROM python:3.8-slim

WORKDIR /app


COPY . .
# runs the pip install command for all packages listed in the requirements.txt file
RUN pip install -r requirements.txt