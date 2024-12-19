import requests
from db import Database
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
cantidadEstados = int(config['DEFAULT']['estadossubidos'])
DB = Database()
response = requests.get("https://dolarbo.com/exchange-rates.json")

def saveNewElapsedDaysValue():
    config['DEFAULT']['estadossubidos'] = str(len(dolarEstadosList))
    with open('config.ini', 'w') as configfile:
        config.write(configfile)


if response.status_code == 200:
    dolarEstadosList = response.json()[0]["history"]
    # for dolarday in dolardayslist:
    #     print(dolarday['timestamp'])
    #     #print(datetime.strptime(dolarday['timestamp'],"%Y-%m-%dT%H:%M:%SZ"))
    
    if cantidadEstados < len(dolarEstadosList):     
        estadosToUpdate = len(dolarEstadosList) - cantidadEstados
        for i,estado in enumerate(dolarEstadosList[-int(estadosToUpdate):]):
            DB.insertNewState(estado['timestamp'],estado['buy'],estado['sell'])
            print(i,estado)
        saveNewElapsedDaysValue()



