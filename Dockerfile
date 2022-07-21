# Build react app
FROM node:18.6-alpine3.15 AS builder
WORKDIR builder
ADD frontend/ .
RUN npm install --loglevel verbose
RUN npm run build

# Build project
FROM python:3.8.13-alpine3.16

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# System deps:
RUN apk update && apk add gcc libc-dev libffi-dev libpq-dev python3-dev zlib-dev jpeg-dev musl-dev
RUN python -m pip install --upgrade pip
RUN pip install "poetry==1.1.13"

# Copy only requirements to cache them in docker layer
WORKDIR /app
COPY poetry.lock pyproject.toml .

# Project initialization:
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi --no-dev

# Creating folders, and files for a project:
COPY . .
RUN rm -rf frontend

# Copy react app from buider image
COPY --from=builder builder/build ./frontend/build