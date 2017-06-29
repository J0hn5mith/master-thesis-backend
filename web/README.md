This is the back end and front end of the Pharos project. The back end is built with the Django frame work. The front
end is a mixture between Djangos template features and Vue.js. Roughly, the static parts and the parts which require a
close integration with Django are built on Django features. The more dynamic components such as maps and dynamic lists
are built with Vue.js

# Installation
## Troubleshooting
* Problem psycopg2 libraries not found
    * Reinstall dependencies from `requirements.txt` file

# Run
## Develop
To the project you have to 
* start the Django development server
    * `./manage.py runserver` (Make sure the *virtualenv* is activated)
* the Gulp task watch
    * `gulp watch`

# Contact
[jan.meier @ uzh.ch](mailto:jan.meier@uzh.ch)

