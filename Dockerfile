FROM python:3.9-alpine3.13
LABEL maintainer="https://github.com/victortxc"

# To see the output of my application
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

RUN python -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin pip install -r /tmp/requirements.txt && \
    adduser \
    --disabled-password \
    --no-create-home \
    django-user

ENV PATH="/venv/bin:$PATH"

USER django-user