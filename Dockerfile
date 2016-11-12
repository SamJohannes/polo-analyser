FROM python:3.5

RUN mkdir -p /src
COPY ./requirements.txt /src/requirements.txt

RUN pip3.5 install -r /src/requirements.txt

VOLUME ['/src']
WORKDIR 'src'

