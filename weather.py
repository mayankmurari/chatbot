import requests

def Weather(city):
    api_address = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=907cc9f7f1e2fb5ae0b24ec2af1d8206'
    #city = input('Citi Name :')
    url = api_address
    json_data = requests.get(url).json()
    print(city)
    format_add = json_data['main']
    print(format_add)
    return format_add

