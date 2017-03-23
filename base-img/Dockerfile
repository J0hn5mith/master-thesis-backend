FROM geodjango:version1.0


RUN\ 
    apt-get update && apt-get -y upgrade && \
    #apt-get install -y git unzip nano wget sudo curl build-essential \
    #python python-dev python-pip python-virtualenv \
    #python3 python3-dev python3-pip python3-venv \
    #postgresql-client-common libpq-dev \
    #postgresql postgresql-contrib postgis \
    #libproj-dev libfreexl-dev libgdal-dev gdal-bin && \
    #python -m pip install pip -U && \
    #python3 -m pip install pip -U && \
    apt-get -y install nodejs && \
    apt-get -y install npm && \
    #yarn &&\
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ONBUILD COPY\
    package.json /usr/src/app &&\
    pip install --no-cache-dir -r requirements.txt/

ONBUILD RUN\
    npm instal && \
