# Installation
## Local
* Install the docker tool box from [here](https://www.docker.com/products/docker-toolbox).
* Create a docker machine with the name `dev`
    * `docker-machine create -d virtualbox dev`
* Tell docker that this is the default machine
    * `eval $(docker-machine env dev)`
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
