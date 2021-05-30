# settings.py
## using python-dotenv for setup
from dotenv import load_dotenv

from pathlib import Path
import os

load_dotenv()
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

#retrieving keys and adding them to the project
POESESSID = os.getenv('POESESSID')
DISCORDHOOK = os.getenv('DISCORDHOOK')
GUILDID = os.getenv('GUILDID')