
workon_production:
	eval $(docker-machine env production)
	export ENV_FILE=.env
	export WEB_ENV_FILE=web/.env

workon_staging:
	eval $(docker-machine env staging)
	export ENV_FILE=.env.staging
	export WEB_ENV_FILE=web/.env.staging

