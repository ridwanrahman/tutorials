FROM python:3.10.11-slim-buster
# this ensures that output is printed to the console immediately without delay
ENV PYTHONGUNBUFFERED=1
RUN apt-get update && apt-get upgrade 
RUN apt-get -y install vim

WORKDIR /backend

EXPOSE 8000

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
