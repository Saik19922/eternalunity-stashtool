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

#monitored items for alarms
ANALYSEDITEMS = [
    # LvLW
    'Silverbranch Crude Bow',
    'Quill Rain Short Bow',
    'Storm Cloud Long Bow',
    "Hyrri's Bite Sharktooth Arrow Quiver",
    'Lifesprig Driftwood Wand',
    'Axiom Perpetuum Bronze Sceptre',
    'Redbeak Rusted Sword',
    'The Screming Eagle',
    'The Princess'   
    # LvLG
    'Tabula Rasa Simple Robe',
    'Goldrim Leather Cap',
    'Lochtonial Caress Iron Gauntlets',
    'Wanderlust Wool Shoes',
    'Seven-League Step Rawhide Boots',
    # LvLO
    'Karui Ward Jade Amulet',
    'Blackheart Iron Ring',
    'Praxis Paua Ring',
    'Le Heup of All Iron Ring',
    'Belt of the Deceiver Heavy Belt',
    "Meginord's Girdle Heavy Belt",
    'Perandus Blazon Cloth Belt',
    'String of Servitude Heavy Belt'
]