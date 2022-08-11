import requests

def Weather(city):
    api_address = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid={appid}'
    #city = input('Citi Name :')
    url = api_address
    json_data = requests.get(url).json()
    print(city)
    format_add = json_data['main']
    print(format_add)
    return format_add

