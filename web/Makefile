DOCKER_MACHINE_NAME=dev
VENV_NAME=venv-master_thesis

setup:
	pip install -r requirements.txt

clean:
	/usr/bin/yes | pip uninstall -r requirements.txt

local:
	eval $(docker-machine env ${DOCKER_MACHINE_NAME})
	gulp watch
