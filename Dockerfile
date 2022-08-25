# using ubuntu 20.04 LTS version
FROM ubuntu@sha256:626ffe58f6e7566e00254b638eb7e0f3b11d4da9675088f4781a50ae288f3322 AS builder-image

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
  apt-get upgrade -y && apt-get install --no-install-recommends -y \
  libmysqlclient-dev python3.9 python3.9-dev python3.9-venv python3-pip python3-wheel build-essential && \
	apt-get clean && rm -rf /var/lib/apt/lists/*

RUN python3.9 -m venv /home/python/venv
ENV PATH="/home/python/venv/bin:$PATH"

# install requirements
COPY . .
RUN pip3 install --no-cache-dir wheel
RUN pip3 install --no-cache-dir -r requirements.txt 
RUN pip3 install --no-cache-dir unicorn

FROM ubuntu@sha256:626ffe58f6e7566e00254b638eb7e0f3b11d4da9675088f4781a50ae288f3322 AS runner-image
RUN apt-get update && \
  apt-get upgrade -y && apt-get install --no-install-recommends -y libmysqlclient-dev python3.9 python3-venv && \
	apt-get clean && rm -rf /var/lib/apt/lists/*

#RUN useradd --create-home python
COPY --from=builder-image /home/python/venv /home/python/venv

#USER python
RUN mkdir /home/python/code
WORKDIR  /home/python/code
COPY --chown=python:python ./ .

EXPOSE 8000

# make sure all messages always reach console
ENV PYTHONUNBUFFERED=1

# activate virtual environment
ENV VIRTUAL_ENV=/home/python/venv \
  PATH="/home/python/venv/bin:$PATH"

# CMD ["gunicorn","-b", "0.0.0.0:8000", "-w", "4", "run:app"]