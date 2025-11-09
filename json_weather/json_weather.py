import reqests

serv_api = " https://openweathermap.org/current"

def get_info(city, api):
    parametrs =
    {
        "": city,
        "": api,
        "": "metric",
        "": "ru"
    }
    response = reqests.get(serv_api, params = parametrs)
    if response.status.code == 200:
        data= response.json()
        print(f"Погода в {data['']}: {data['']}, {data['']}")

if __name__ == "__main__":
    api = input()
    city = input()
    get_weather(city,api)
