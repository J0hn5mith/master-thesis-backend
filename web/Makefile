install: install-back-end
	echo "Done"

install-dependencies:
	brew install postgresql
	brew install postgis
	brew install gdal
	brew install libgeoip

install-back-end:
	pip install -r requirements.txt

update: run-migrations
	echo "Done"

migrate: make-migrations run-migrations
	echo "Done"

run-migrations:
	./manage.py migrate

make-migrations:
	./manage.py makemigrations

clean: clean-back-end
	echo "Done"

clean-back-end:
	/usr/bin/yes | pip uninstall -r requirements.txt

check_defined = \
				$(strip $(foreach 1,$1, \
				$(call __check_defined,$1,$(strip $(value 2)))))
__check_defined = \
				  $(if $(value $1),, \
				  $(error Undefined $1$(if $2, ($2))))
