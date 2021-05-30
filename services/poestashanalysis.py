from apis.db import DBApi
from apis.discord import DiscordApi
import settings

class PoeStashAnalysisService:

    def __init__(self):
        self.analyzingRecords = False
        self.db = DBApi()
        self.discord = DiscordApi()

    def analyseRecords(self):
        if(self.analyzingRecords):
            print('Still analyzing previous records.')
            return

        self.analyzingRecords = False

        # First get all known Guild Members
        members = self.db.getAllMembers()

        for member in members:
            transactions = self.db.getAllTransactionsOfMember(member)
            # TODO: IMPLEMENT
            for item in settings.ANALYSEDITEMS:
                pass

