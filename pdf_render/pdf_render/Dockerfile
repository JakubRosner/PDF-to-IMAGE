FROM python:3.9-slim
EXPOSE 8000

RUN mkdir /code

ADD requirements.txt ./

RUN apt-get update && apt-get -y install poppler-utils && apt-get clean
RUN pip install -r requirements.txt

ADD ./ /code/

WORKDIR /code
