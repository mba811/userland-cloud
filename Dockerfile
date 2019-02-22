FROM python:3.7-slim
MAINTAINER cypherpunkarmory

RUN pip install pipenv

ARG APP_NAME
ENV APP_HOME /$APP_NAME
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

ADD Pipfile.lock $APP_HOME/Pipfile.lock
ADD Pipfile $APP_HOME/Pipfile
RUN pipenv install --system --dev

CMD bash

