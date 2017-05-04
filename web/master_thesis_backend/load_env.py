from os.path import dirname, join
import os
import dotenv


def load_env(develop=False):
    """
    Get the path to the .env file and load it. If the 'DJANGO_SETTINGS_MODULE'
    env variable is set it's assumed that all other variables are set as well
    and no file is loaded.
    """

    if not os.environ.get('DJANGO_SETTINGS_MODULE', False):
        project_dir = dirname(dirname(__file__))
        if develop:
            dotenv.read_dotenv(join(project_dir, '.env.local'))
        else:
            dotenv.read_dotenv(join(project_dir, '.env'))
