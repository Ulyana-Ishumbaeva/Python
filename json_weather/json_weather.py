import requests

serv_api = "https://api.openweathermap.org/data/2.5/weather"

def get_info(city, api):
    parametrs ={
        "q": city,
        "appid": api,
        "units": "metric",
        "lang": "ru"
    }
    response = requests.get(serv_api, params = parametrs)
    if response.status_code == 200:
        data= response.json()
        #print(data)
        print(f"Погода в {data['name']}: {data['weather'][0]['description']},{data['main']['temp']}°")

if __name__ == "__main__":
    api = '746c9ab9cf6b08ea270ed1a4c906841c'
    city = input()
    get_info(city,api)
