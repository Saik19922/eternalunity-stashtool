from datetime import datetime

import requests
import settings

class DiscordApi:

    def __init__(self):
        self.hook = settings.DISCORDHOOK

    # TODO: Append multiple transactions
    def sendPoeStashTransactionToDiscord(self, entry):
        formattedDate = datetime.utcfromtimestamp(entry["time"]).strftime('%Y-%m-%d %H:%M:%S')
        data = {
            "avatar_url": "https://web.poecdn.com/image/Art/2DItems/Currency/CurrencyAddModToRare.png",
            "content": "{0}: {1} **{2}** item '{3}' in **{4} League**".format(formattedDate, entry["account"]["name"], entry["action"], entry["item"], entry["league"])
        }

        result = requests.post(self.hook, json = data)

        try:
            result.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(err)
        else:
            print("Payload delivered successfully, code {}.".format(result.status_code))

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

    def generateEmbeds(self):
        embeds = [{
            "title": "Hello!",
            "description": "Hi! :grinning:"
        }]

        return embeds