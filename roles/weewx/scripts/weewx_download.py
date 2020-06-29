import json

import requests

import wget

req_data = requests.get("https://api.github.com/repos/weewx/weewx/releases")

data = req_data.json()

latest_full = (data[0]["tag_name"])

latest = latest_full.strip("v")


url = "http://weewx.com/downloads/weewx-" + latest + ".tar.gz"
name = "weewx.tar.gz"


try:
    wget.download(url, name)
except:
    latest_full = (data[1]["tag_name"])
    latest = latest_full.strip("v")
    name = "weewx-" + latest + ".tar.gz"
    url = "http://weewx.com/downloads/weewx-" + latest + ".tar.gz"
    wget.download(url, name)
