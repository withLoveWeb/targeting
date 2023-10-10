FROM python:3.10

WORKDIR /usr/src/elastic

COPY ./requirements.txt /usr/src/requirements.txt
RUN pip3 install -r /usr/src/requirements.txt

COPY . /usr/src/elastic