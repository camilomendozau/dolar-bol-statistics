import requests
#from bs4 import BeautifulSoup
import json
from datetime import datetime
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
daysElapsed = int(config['DEFAULT']['DAYSELAPSED'])

response = requests.get("https://dolarbo.com/exchange-rates.json")

def saveNewElapsedDaysValue(updatedDays):
    config['DEFAULT']['DAYSELAPSED'] = str(len(dolardayslist))
    with open('config.ini', 'w') as configfile:
        config.write(configfile)


if response.status_code == 200:
    dolardayslist = response.json()[0]["history"]
    for dolarday in dolardayslist:
        print(dolarday['timestamp'])
        #print(datetime.strptime(dolarday['timestamp'],"%Y-%m-%dT%H:%M:%SZ"))
    
    if daysElapsed < len(dolardayslist):
        
        daysToUpdate = len(dolardayslist) - daysElapsed
        saveNewElapsedDaysValue(daysElapsed)
        #print(daysElapsed)
    # for day in dolardayslist:
    #     print(day["timestamp"])
    #     print(day["buy"])
    #     print(day["sell"])



