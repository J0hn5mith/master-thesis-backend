from os.path import dirname, join
import os
import dotenv


def load_env(develop=False):
    "Get the path to the .env file and load it."

    # If settings module is set we assume that we have a properly setup env
    # if os.environ.get('DJANGO_SETTINGS_MODULE', False):
        # return

    project_dir = dirname(dirname(__file__))
    if develop:
        dotenv.read_dotenv(join(project_dir, '.env.local'))
    else:
        dotenv.read_dotenv(join(project_dir, '.env'))
