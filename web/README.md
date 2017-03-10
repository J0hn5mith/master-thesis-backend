This is the back end and front end of the Pharos project. The back end is built with the Django frame work. The front
end is a mixture between Djangos template features and Vue.js. Roughly, the static parts and the parts which require a
close integration with Django are built on Django features. The more dynamic components such as maps and dynamic lists
are built with Vue.js

# Installation
* Install [`yarn`](https://yarnpkg.com/en/docs/usage)
* Install [`virtualenv`](https://virtualenv.pypa.io/en/stable/)
* Install [`virtualenv-wrapper`](http://virtualenvwrapper.readthedocs.io/en/latest/)
* Create a new *virtualenv*. (Make sure you are using python 3.x)
* Run `make install` (if you don't have make installed use brew to do so: `brew install make`)


# Run
## Develop
To the project you have to 
* start the Django development server
    * `./manage.py runserver` (Make sure the *virtualenv* is activated)
* the Gulp task watch
    * `gulp watch`

# Contact
[jan.meier @ uzh.ch](mailto:jan.meier@uzh.ch)

# License
MIT License

Copyright (c) 2017 Jan Meier

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

<!--# Python Libraries-->
<!--* Django REST Framework -> http://www.django-rest-framework.org/api-guide/routers/-->

<!--# Backend-->
<!--# Style and Conventions-->
<!--The coding style follows a based PEP-8 convention. Further, the yapf source code formater for pyton is used with the-->
<!--following settings:-->
<!--```-->
<!--[style]-->
<!--based_on_style = pep8-->
<!--ALIGN_CLOSING_BRACKET_WITH_VISUAL_INDENT = true-->
<!--DEDENT_CLOSING_BRACKETS = true-->
<!--```-->
<!--https://www.python.org/dev/peps/pep-0008/#indentation-->
<!--https://github.com/google/yapf-->


<!--# Webpack and Vue-->
<!--https://pagekit.com/docs/developer/vuejs-and-webpack-->


<!--# JS Libraries-->
<!--* axios -> Dealing with clientside AJAX-->

