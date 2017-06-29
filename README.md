# Installation
## Develop
* Install the docker tool box from [here](https://www.docker.com/products/docker-toolbox).
* Clone the following docker image into the root folder of the project
    * `git clone https://github.com/J0hn5mith/docker-nginx-letsencrypt-proxy.git`
* Create a docker machine with the name `dev`
    * `docker-machine create -d virtualbox dev`
* Create `.env.dev` file
    * set the environment variables according to the one in the `.env.example` file
* Do the same for the `web/.env.dev` (`web/.env.example`)
* set the environment variables
    * `./set_env.sh dev `
* Build the front end. The details are explained further down in this readme file.
* Build the docker images
    * `docker-compose build`
* Mount the docker containers containers
    * `docker-compose up -d`
*(Hint: This project is based on this [tutorial](https://realpython.com/blog/python/django-development-with-docker-compose-and-machine/).)*

# Deployment
Create the deployment docker machine. Follow the steps from the local installation but with distinct `.env` files.


# Local Mode
The local mode is based on the develop hosting described above. However, the back end and optionally the front end are
hosted locally.
## Install Back End Locally
(This instructions work on MacOS)

* Install [`virtualenv`](https://virtualenv.pypa.io/en/stable/)
* Install [`virtualenv-wrapper`](http://virtualenvwrapper.readthedocs.io/en/latest/)
* Create a new *virtualenv*. (Make sure you are using python 3.x)
    * `mkvirtualenv your-env-name`
* Install libraries required by GeoDjango
    * Run `make install-dependencies`
* Run `make install` (if you don't have make installed use brew to do so: `brew install make`)
* Run `make update`

## Run Back End Locally
* Create the `env.local` file and set the settings for the local hosting in the  `web` folder
    * Set `DOMAIN=localhost:8000`
    * If you want to run the front end locally as well set `FRONTEND_URL=http://localhost:8001/`
    * The other variables should be the same as for the develop setup.
* `./manage.py runserver` (Make sure the *virtualenv* is activated)

## Run Front End Locally
* Change to the front end dir
* Build the front end
    * `gulp build`
* Run the local file server
    * `gulp watch`





FAQ:
* How can I execute commands for the single application components?
    * First attach yourself to the running docker image `docker exec -it <image_name> bash`
    * Then you get a command line which is located inside the running docker iamge.
    * Attention: The linux distributions are reduced to a minimum and some commonly available tools are not installed!

## Build frontend
* `gulp build`

# Settings
| Parameter | Description  |
| --------- | -----------  |
| `STATIC_FILE_URL` | URL where the front end files are hosted. |
| `TILE_SET_URL` | URL for the tile's used for the map. |
| `DEBUG` |  Toggle for debug mode. |


# Front end
## Installation Front end
* Install NPM
    * https://nodejs.org/en/
* Install yarn
    * https://yarnpkg.com/lang/en/docs/install/
* Run yarn to install front end packages
* Install gulp
    * http://gulpjs.com/
* Install sass
    * http://sass-lang.com/

## Gulp Commands
| Command | Description  |
| --------- | -----------  |
| `clean` | Removes all build files (all the files in the static folder) and all intermediate files. |
| `watch` | Used for development. |
| `build` | Builds the front end. |

## Update Frontend
1. Run command `gulp build` in this folder to create the files in the static folder
2. Stop the running containers if necessary. (`docker-compose stop`)
3. Create or rebuild the `frontend` docker image (`docker-compose build --no-cache frontend`)
4. Restart the containers (`docker-compose up -d`)

If the front end files were not updated, delete the `frontend` docker volume between step 2 and 3.
