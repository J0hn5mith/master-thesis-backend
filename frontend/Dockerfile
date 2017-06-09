FROM buildpack-deps:jessie

RUN rm -rf /usr/src/frontend/ # Delete previous version
RUN mkdir -p /usr/src/frontend/

WORKDIR /usr/src/frontend/
COPY ./static/ /usr/src/frontend/
