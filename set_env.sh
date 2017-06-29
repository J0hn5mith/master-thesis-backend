#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'


if [[ -z ${1+x} ]]; then
    >&2 echo "Pleas provide a env you would like to work on"
    exit 1;
fi

if [[ $1 == dev ]]; then
    echo "export WEB_ENV_FILE=web/.env.develop"
    echo "export ENV_FILE=.env.develop"
    docker-machine env dev
    exit 0;
fi

if [[ $1 == staging ]]; then
    echo "export WEB_ENV_FILE=web/.env.staging"
    echo "export ENV_FILE=.env.staging"
    docker-machine env staging
    exit 0;
fi

if [[ $1 == production ]]; then
    echo "export WEB_ENV_FILE=web/.env"
    echo "export ENV_FILE=.env"
    docker-machine env productin
    exit 0;
fi

if [[ $1 == csg ]]; then
    echo "export WEB_ENV_FILE=web/.env.csg"
    echo "export ENV_FILE=.env.csg"
    docker-machine env csg
    exit 0;
fi

exit 1;

