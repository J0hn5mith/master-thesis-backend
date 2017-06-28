# Installation Backend
## Local
* Install the docker tool box from [here](https://www.docker.com/products/docker-toolbox).
* Clone the following docker image into the root folder of the project
    * `git clone https://github.com/J0hn5mith/docker-nginx-letsencrypt-proxy.git`
* Create a docker machine with the name `dev`
    * `docker-machine create -d virtualbox dev`
* Tell docker that this is the default machine
    * `eval $(docker-machine env dev)`
* Create volumes
    * `docker volume create --name=pgdata`
    * `docker volume create --name=pgisdata`
* set env variables `ENV_FILE` and `WEB_ENV_FILE` to corresponding paths
    *  `ENV_FILE=.env.develop`
    *  `ENV_FILE=.web/env.develop`
* Build the docker images
    * `docker-compose build`
* Mount the docker containers containers
    * `docker-compose up -d`
* Create a database with name `postgres`
* Create a user `postgres` with the password `postgres` and grant him all rights for the `postgres` database

*(Hint: This project is based on this [tutorial](https://realpython.com/blog/python/django-development-with-docker-compose-and-machine/).)*


FAQ:
* How can I execute commands for the single application components?
    * First attach yourself to the running docker image `docker exec -it <image_name> bash`
    * Then you get a command line which is located inside the running docker iamge.
    * Attention: The linux distributions are reduced to a minimum and some commonly available tools are not installed!

## Deployment
* Docker Workflow
* set env variables `ENV_FILE` and `WEB_ENV_FILE` to corresponding paths

# Installation Front end
* Install NPM
    * https://nodejs.org/en/
* Install yarn
    * https://yarnpkg.com/lang/en/docs/install/
* Run yarn to install front end packages
* Install gulp
    * http://gulpjs.com/
* Install sass
    * http://sass-lang.com/

## Build frontend
* `gulp build`
