# Setup instructions

(optional) create a python environment and activate it
    python -m venv env
    env\Scripts\activate

install dependancies
    pip install -r requirements.txt

create a .env in the project root and add the following to it (fill out <AREAS> with your keys/hooks/guildid)
    POESESSID='<POESESSID HERE>'
    DISCORDHOOK='<DISCORDHOOK HERE>'
    GUILDID=<GUILDID HERE>

Then just run `pytests tests.py` to see if everything works properly or run main.py directly.