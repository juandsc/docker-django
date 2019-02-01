FROM python:3.6
MAINTAINER juansanchezc89@gmail.com

#Enviroment variables
ENV USER=tester
ENV HOME_DIR=home/tester
ENV ENTRY_DIR=entry_folder
ENV LOGS_DIR=logs
ENV SHELL=/bin/bash

# Install packages necesary
RUN pip install --upgrade pip
RUN mkdir /tmp/requirements
COPY ./test_app/requirements/base.txt /tmp/requirements
COPY ./test_app/requirements/prod.txt /tmp/requirements
RUN pip install -r /tmp/requirements/prod.txt

#Entry-point
RUN mkdir /$ENTRY_DIR
COPY ./docker/prod/python/entrypoint.sh /$ENTRY_DIR
RUN chmod +x /$ENTRY_DIR/entrypoint.sh
RUN ./$ENTRY_DIR/entrypoint.sh

RUN mkdir /$LOGS_DIR

#Set up user not root
RUN useradd -ms $SHELL $USER
RUN mkdir -p /$HOME_DIR
RUN chown -R $USER:$USER /$HOME_DIR

USER $USER
WORKDIR /$HOME_DIR/
