import requests
def currency_exchange():
    url = f'https://www.cbr-xml-daily.ru/latest.js'
    weather_parameters = {
        'format': 2,
        'M': ''
    }

    response = requests.get(url, params=weather_parameters).text
    data = eval(response)
    TRY_rate = data.setdefault('rates').setdefault('TRY')
    Money_TRY = TRY_rate * 100 / 10 + 0.5

    return Money_TRY