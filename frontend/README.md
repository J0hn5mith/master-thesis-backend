# Installation Front end
* Install NPM
    * https://nodejs.org/en/
* Install yarn
    * https://yarnpkg.com/lang/en/docs/install/
* Run yarn to install front end packages
* Install gulp
    * http://gulpjs.com/
* Install sass
    * http://sass-lang.com/

# Gulp Commands
| Command | Description  |
| --------- | -----------  |
| `clean` | Removes all build files (all the files in the static folder) and all intermediate files. |
| `watch` | Used for development. |
| `build` | Builds the front end. |

# Update Frontend
1. Run command `gulp build` in this folder to create the files in the static folder
2. Stop the running containers if necessary. (`docker-compose stop`)
3. Create or rebuild the `frontend` docker image (`docker-compose build --no-cache frontend`)
4. Restart the containers (`docker-compose up -d`)

If the front end files were not updated, delete the `frontend` docker volume between step 2 and 3.

