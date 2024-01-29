FROM python:3.12-alpine3.19
LABEL maintainer="Kathleen Avvento"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./api /api
WORKDIR /api
EXPOSE 8000

RUN python3 -m venv /py && \
    /py/bin/pip3 install --upgrade pip && \
    /py/bin/pip3 install -r /tmp/requirements.txt && \
    rm -rf /tmp && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

ENV PATH="/py/bin:$PATH"

USER django-user
