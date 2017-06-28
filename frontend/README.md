# Set Up
1) Install yarn

# Settings
The settings for the front end are defined in the `webpack.config.js` files. The following settings are available:
| Parameter | Description  |
| --------- | -----------  |
| `STATIC_FILE_URL` | URL where the front end files are hosted. |
| `TILE_SET_URL` | URL for the tile's used for the map. |
| `DEBUG` |  Toggle for debug mode. |

# Gulp Commands
| Command | Description  |
| --------- | -----------  |
| `clean` | Removes all build files (all the files in the static folder) and all intermediate files.|
| `watch` | The front end's main 
watch

# Update Frontend
1. Run command `gulp build` in this folder to create the files in the static folder
2. Stop the running containers if necessary. (`docker-compose stop`)
3. Create or rebuild the `frontend` docker image (`docker-compose build --no-cache frontend`)
4. Restart the containers (`docker-compose up -d`)

If the front end files were not updated, delete the `frontend` docker volume between step 2 and 3.

