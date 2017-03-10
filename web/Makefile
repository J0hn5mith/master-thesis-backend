install: install-back-end install-front-end
	echo "Done"

install-back-end:
	pip install -r requirements.txt

install-front-end:
	yarn install

update: run-migrations
	echo "Done"

migrate: make-migrations run-migrations
	echo "Done"

run-migrations:
	./manage.py migrate

make-migrations:
	./manage.py makemigrations

clean: clean-back-end clean-front-end
	echo "Done"

clean-back-end:
	/usr/bin/yes | pip uninstall -r requirements.txt

clean-front-end:
	rm -r ./node_modules
