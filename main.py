import requests,time
from db import Database
import configparser



#response = requests.get("https://dolarbo.com/exchange-rates.json")

def saveNewElapsedDaysValue(dolarEstadosList):
    config['DEFAULT']['estadossubidos'] = str(len(dolarEstadosList))
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

def fetch_data_from_api():
    try:
        response = requests.get('https://dolarbo.com/exchange-rates.json')
        if response.status_code == 200:
            DB = Database()
            dolarEstadosList = response.json()[0]["history"]
            if cantidadEstados < len(dolarEstadosList):
                estadosToUpdate = len(dolarEstadosList) - cantidadEstados
                for i, estado in enumerate(dolarEstadosList[-int(estadosToUpdate):]):
                    DB.insertNewState(estado['timestamp'], estado['buy'], estado['sell'])
                    print(i, estado)
                saveNewElapsedDaysValue(dolarEstadosList)
            DB.closeConexion()
        else:
            print(f"Error en la consulta: {response.status_code}")
    except Exception as e:
        print(f"Error al conectar con la API: {e}")

def main():
    while True:
        fetch_data_from_api()
        time.sleep(120)

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config.ini')
    cantidadEstados = int(config['DEFAULT']['estadossubidos'])
    main()
