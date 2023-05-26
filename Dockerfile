# pull official base image
FROM python:3.11.3

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy project
COPY . /usr/src/app/

# install dependencies
RUN pip install --upgrade pip setuptools wheel \
    && pip install -r /usr/src/app/src/requirements.txt \
    && rm -rf /root/.cache/pip
