from datetime import datetime
import time

import requests
import settings

class DiscordApi:

    def __init__(self):
        self.hook = settings.DISCORDHOOK

    def sendManyPoeWarningsToDiscord(self, data):
        # First check how many Warnings we still have to notify for (for example 11 warnings have been split and this is the second message)
        if(len(data) == 1):
            self.sendPoeWarningToDiscord(data[0])
        else:
            embeds = []
            for d in data:
                fields = self.generateFieldsFromWarningData(d["wd"])
                embed = {
                    "title": d["member"],
                    "description": d["ds"],
                    "fields": fields
                }
                embeds.append(embed)
            postData = {
                "avatar_url": "https://web.poecdn.com/image/Art/2DItems/Currency/CurrencyAddModToRare.png",
                "content": "Warning from PoE Stashtool for multiple Members",
                "embeds": embeds
            }

            result = requests.post(self.hook, json = postData)

            try:
                result.raise_for_status()
            except requests.exceptions.HTTPError as err:
                print(err)
            else:
                print("Payload delivered successfully, code {}.".format(result.status_code))

            time.sleep(5)

    # TODO: Append multiple transactions
    def sendPoeWarningToDiscord(self, data):
        fields = self.generateFieldsFromWarningData(data["wd"])
        postData = {
            "avatar_url": "https://web.poecdn.com/image/Art/2DItems/Currency/CurrencyAddModToRare.png",
            "content": "Warning from PoE Stashtool for Member: " + data["member"],
            "embeds": [{
                "title": data["ds"],
                "fields": fields
            }]
        }

        result = requests.post(self.hook, json = postData)

        try:
            result.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(err)
        else:
            print("Payload delivered successfully, code {}.".format(result.status_code))

        time.sleep(5)

    # TODO: Move to discord api module
    def sendHelloWorldToDiscord(self):
        embeds = self.generateEmbeds()

        data = {
            "avatar_url": "https://web.poecdn.com/image/Art/2DItems/Currency/CurrencyAddModToRare.png",
            "content": 'Hello world!',
            "username": 'FooBot',
            "embeds": embeds
        }

        result = requests.post(self.hook, json = data)

        try:
            result.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(err)
        else:
            print("Payload delivered successfully, code {}.".format(result.status_code))

    def generateFieldsFromWarningData(self, wd):
        fields = []
        for warning in wd:
            field = {
                "name": warning["item"],
                "value": "Item Delta: " + warning["delta"]
            }
            fields.append(field)
        return fields