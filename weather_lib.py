import json
import requests
import openmeteo_requests

def fetchLocation(place : str):
    #Nomes compostos precisam ser tratados,o caracter " " precisa ser trocado por "+"
    place = place.replace(" ","+")
    res = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={place}&count=1&language=en&format=json")
    jsonData = json.loads(res.text)
    coordenadas = [jsonData['results'][0]['latitude'],jsonData['results'][0]['longitude']]
    return weatherDailyParams(coordenadas)


def weatherDailyParams(place:list):
    #days = int(input("Quantidade de dias: "))
    params = {
            "latitude": place[0],
            "longitude": place[1],
            "daily": ["temperature_2m_max", "temperature_2m_min", "sunrise", "sunset"],
            "forecast_days": 3
            }
    return params

def resquestData(parametros:str):
    cliente = openmeteo_requests.Client()
    responses = cliente.weather_api("https://api.open-meteo.com/v1/forecast",params=parametros)
    response = responses[0]#Salva o primeiro resultado da pesquisa
    return response

