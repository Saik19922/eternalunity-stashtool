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
        pendingWarnings = []
        for member in members:
            transactions = self.db.getAllTransactionsOfMember(member)
            # TODO: IMPLEMENT
            transactionsSorted = []
            totalAdd, totalRem, totalEdit = 0, 0, 0
            for item in settings.ANALYSEDITEMS:
                add, rem, edit = 0, 0, 0
                for transaction in transactions:
                    if(transaction[3] == item):
                        if(transaction[2] == 'added'):
                            add += 1
                        elif(transaction[2] == 'removed'):
                            rem += 1
                        elif(transaction[2] == 'edited'):
                            edit += 1
                if(add - rem < 0):
                    itemSorted = {"item": item, "added": add, "removed": rem, "delta": add-rem, "edited": edit}
                    transactionsSorted.append(itemSorted)
                totalAdd += add
                totalRem += rem
                totalEdit += edit
            if(len(transactionsSorted) > 0 and (totalAdd - totalRem) <= settings.TOTALDEBT):
                memberName = member[0]
                warningData = []
                totalDeltaString = ""
                for transaction in transactionsSorted:
                    warningData.append({"item": transaction["item"], "delta": str(transaction["delta"])})
                totalDeltaString = "Total Delta: " + str(totalAdd - totalRem)
                pendingWarnings.append({"member": memberName, "wd": warningData, "ds": totalDeltaString})
        if(len(pendingWarnings) > 10):
            splittedWarnings = chunks(pendingWarnings, 10)
            for w in splittedWarnings:
                self.discord.sendManyPoeWarningsToDiscord(w)
        elif(len(pendingWarnings) > 1):
            self.discord.sendManyPoeWarningsToDiscord(pendingWarnings)
        elif(len(pendingWarnings == 1)):
            self.discord.sendPoeWarningToDiscord(pendingWarnings[0])
        else:
            print("No baddies found. For now.")

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]        