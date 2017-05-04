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
    exit 0;
fi

if [[ $1 == staging ]]; then
    echo "export WEB_ENV_FILE=web/.env.staging"
    echo "export ENV_FILE=.env.staging"
    exit 0;
fi

if [[ $1 == deploy ]]; then
    echo "export WEB_ENV_FILE=web/.env.deploy"
    echo "export ENV_FILE=.env.deploy"
    exit 0;
fi

exit 1;

