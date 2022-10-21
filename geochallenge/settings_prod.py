"""
This file is the setting file for the production environment.
It's override the default settings.py file, which is used for development.
"""

import geochallenge.settings
import os
import dotenv # <- New

# Add .env variables anywhere before SECRET_KEY
dotenv_file = os.path.join(".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

if "SECRET_KEY" not in os.environ or not os.environ["SECRET_KEY"]:
    exit("No SECRET_KEY set for Django, aborting for safety.")

DEBUG = False
SECRET_KEY = os.environ["SECRET_KEY"]
ALLOWED_HOSTS = [
    "flagle.gwenael-leger.fr",
    "flagle-api.gwenael-leger.fr",
]

