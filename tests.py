from unittest.mock import Mock, patch
from apis.poe import PoeHttpApi
import time

# TODO: Add Mock to API Tests!

class TestApiPoe:

    def test_guildstashhistory(self):
        # Instantiate PoeHttpApi
        api = PoeHttpApi('Saik1992', 'Ultimatum')

        recent = api.get_guildstashrecenthistory()
        # Setup last element for next test
        last = recent[-1]
        # Response of recent stash history should not be None or Empty with a valid POESESSID
        assert recent != None
        assert len(recent) > 0

        response = api.get_guildstashhistory(last["time"], last["id"])

        # Response of stashhistory should not be None or Empty with a valid POESESSID
        assert response != None
        assert len(response) > 0