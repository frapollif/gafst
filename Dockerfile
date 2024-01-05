FROM python:3.10-slim
ENV PYTHONBUFFERED=1
RUN mkdir /code
WORKDIR /code
