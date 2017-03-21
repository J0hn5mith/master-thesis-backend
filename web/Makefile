FRONT_END_BASE=./frontend
HTML=${FRONT_END_BASE}/html/
VUE_COMPONENTS=${FRONT_END_BASE}/js/vue-components/

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
	rm -r ./static/

check_defined = \
    $(strip $(foreach 1,$1, \
        $(call __check_defined,$1,$(strip $(value 2)))))
__check_defined = \
    $(if $(value $1),, \
      $(error Undefined $1$(if $2, ($2))))

vue-component:
	$(call check_defined, NAME)
	@touch ${HTML}${NAME}.html
	@touch ${VUE_COMPONENTS}${NAME}.vue
	@touch ${VUE_COMPONENTS}script/${NAME}.js
	@echo "<template src=\"./../../html/${NAME}.html\"></template>" >> ${VUE_COMPONENTS}${NAME}.vue
	@echo "<script src=\"./script/${NAME}.js\"></script>" >> ${VUE_COMPONENTS}${NAME}.vue
