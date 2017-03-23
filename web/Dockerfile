FROM python:3.5-onbuild

RUN apt-get update && apt-get -y upgrade && \
    apt-get install -y git unzip nano wget sudo curl build-essential \
    python python-dev python-pip python-virtualenv \
    python3 python3-dev python3-pip python3-venv \
    postgresql-client-common libpq-dev \
    postgresql postgresql-contrib postgis \
    libproj-dev libfreexl-dev libgdal-dev gdal-bin && \
    python -m pip install pip -U && \
    python3 -m pip install pip -U && \
    #apt-get install nodejs && \
    #apt-get  install yarn && \
    #yarn &&\
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
