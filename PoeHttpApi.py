import requests
import json
import urllib.parse
import time
import cloudscraper
import re
import string

class PoeHttpApi:
    ssid_cookie = ""
    account_name = ""
    league = ""
    realm = "pc"
    # change guild id in the link
    url_guild = "https://www.pathofexile.com/api/guild/353917/stash/history"

    def __init__(self, account_name, league, ssid, realm="pc"):
        self.account_name = account_name
        self.league = league
        self.ssid_cookie = {'POESESSID': ssid}
        self.realm = realm
        self.session = cloudscraper.create_scraper(interpreter='nodejs')

    # @limits(calls=29, period=60)
    def get_guildstashrecenthistory(self):
        response = self.session.get(self.url_guild, cookies=self.ssid_cookie)

        # response = requests.post(url, cookies=self.ssid_cookie)
        if response:
            res = json.loads(response.content)["entries"]
            return res
        elif response.status_code == 429:
            print("API rate limit exceeded, waiting for {0} seconds".format(response.headers["Retry-After"]))
            time.sleep(int(response.headers["Retry-After"]))
        else:
            print("HTTP-Statuscode: ", response.status_code)

    def get_guildstashhistory(self, fromEpochTime, fromId):
        url_vars = {"from": fromEpochTime, "fromId": fromId}

        url = "".join((self.url_guild, "?", urllib.parse.urlencode(url_vars)))
        response = self.session.get(url, cookies=self.ssid_cookie)

        # response = requests.post(url, cookies=self.ssid_cookie)
        if response:
            res = json.loads(response.content)["entries"]
            return res
        elif response.status_code == 429:
            print("API rate limit exceeded, waiting for {0} seconds".format(response.headers["Retry-After"]))
            time.sleep(int(response.headers["Retry-After"]))
            return False
        else:
            print("HTTP-Statuscode: ", response.status_code)
            return False
