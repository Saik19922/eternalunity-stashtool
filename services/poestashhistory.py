from apis.poe import PoeHttpApi
from apis.db import DBApi
from apis.discord import DiscordApi

class PoeStashHistoryService:

    def __init__(self):
        self.processingRecords = False
        self.api = PoeHttpApi("Saik1992", "Ultimatum")
        self.db = DBApi()
        self.discord = DiscordApi()

    def processRecords(self):
        if(self.processingRecords):
            print('Still processing previous records.')
            return

        self.processingRecords = True

        allRecords = []

        recent_history = self.api.get_guildstashrecenthistory()
        if(recent_history == False or len(recent_history) == 0):
            print(
                'Error while obtaining data or no data obtained (Should only happen when servers are down')
            self.processingRecords = False
            return

        lastRecordedRecord = self.db.findLatestRecord()

        if(lastRecordedRecord["id"] == None):
            # "Start from scratch", basically
            lastRecordedRecord = {"id": 0, "time": 0}

        print("Last recorded record: ID:[{0}], epoch[{1}]".format(
            lastRecordedRecord["id"], lastRecordedRecord["time"]))

        continueProcessing = True
        bailoutCounter = 0
        loopResult = self.loopProcess(recent_history, lastRecordedRecord)
        continueProcessing = loopResult["continueProcessing"]

        if(len(loopResult["entries"]) > 0):
            allRecords.extend(loopResult["entries"])
            self.db.insertMany(loopResult["entries"])

        while continueProcessing:
            last = loopResult["entries"][-1]
            jr = self.api.get_guildstashhistory(last["time"], last["id"])
            if(jr == None):
                print("API Limiting hit us, or some other Error occured. Trying again.")
            elif(len(jr) == 0):
                bailoutCounter += 1
                print(
                    "No records recieved for processing. ({0}/3)".format(bailoutCounter))
            else:
                loopResult = self.loopProcess(jr, lastRecordedRecord)
                if(len(loopResult["entries"]) > 0):
                    allRecords.extend(loopResult["entries"])
                    self.db.insertMany(loopResult["entries"])

            if(bailoutCounter > 2):
                continueProcessing = False
            else:
                continueProcessing = loopResult["continueProcessing"]

        # TODO: Add actual data validation

        #if(len(allRecords) > 0):
        #    for record in allRecords:
        #        self.discord.sendPoeStashTransactionToDiscord(record)

        self.processingRecords = False

    def loopProcess(self, responseEntries, lastRecordedRecord):
        entries = []
        continueProcessing = True
        if(len(responseEntries) > 0):
            for x in responseEntries:
                print("RecordId = {0}/{1} vs {2}/{3} == {4}".format(
                    x["id"], x["time"], lastRecordedRecord["id"], lastRecordedRecord["time"], x["id"] == lastRecordedRecord["id"]))
                if(x["id"] == lastRecordedRecord["id"]):
                    continueProcessing = False
                    print(
                        "No more records to process, setting continueProcessing to false.")
                    break
                else:
                    entries.append(x)
        else:
            continueProcessing = False
            print("No more records to process, setting continueProcessing to false.")
        print("Continue processing: ", continueProcessing)
        return {"entries": entries, "continueProcessing": continueProcessing}