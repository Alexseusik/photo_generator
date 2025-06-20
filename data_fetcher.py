import requests
from bs4 import BeautifulSoup
from datetime import datetime
import locale

weather_api = "58c4b2e9a9b2565b6ab85e8afb62527a"


def make_request(url, headers=None):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response
    except requests.RequestException as e:
        print(f"Помилка запиту: {e}")
        return None


def parse_currency_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    currency_data = soup.find_all('div', {'class': 'sc-1x32wa2-9',
                                          'type': 'average'})[:4]

    for item in currency_data:
        for child in item.find_all(recursive=True):
            child.decompose()

    currency_data = ["{:.2f}".format(float(rate.text.replace(',','.'))) for rate in currency_data]

    return {
        'usd': {
            'buy' : currency_data[0],
            'sell': currency_data[1]
        },
        'eur': {
            'buy' : currency_data[2],
            'sell': currency_data[3]
        }
    }


def parse_oil_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    oil_data = soup.find_all('big')
    return {
        'A95': oil_data[1].text.replace(',', '.'),
        'diesel': oil_data[3].text.replace(',', '.'),
        'gas': oil_data[4].text.replace(',', '.')
    }


def get_weather_iconid(city_name, api_key):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            return f"{data['weather'][0]['icon']}"
        else:
            return "Помилка при отриманні погоди"
    except requests.RequestException:
        return "Не вдалося виконати запит на погоду"


def get_weather(city_name, api_key):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            return f"{round(data['main']['temp'])}°C"
        else:
            return "Помилка при отриманні погоди"
    except requests.RequestException:
        return "Не вдалося виконати запит на погоду"


def get_bitcoin_price():
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
        response = requests.get(url)
        data = response.json()
        return data['bitcoin']['usd']
    except requests.RequestException:
        return "Не вдалося виконати запит на ціну біткоїна"


def get_all_data():

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    currency_url = "https://minfin.com.ua/ua/currency"
    oil_url = "https://index.minfin.com.ua/ua/markets/fuel/"

    currency_response = make_request(currency_url, headers)
    oil_response = make_request(oil_url, headers)

    today_date_str = datetime.now().strftime('%d.%m.%Y')

    # Встановлення дефолтних значень як None
    all_data = {}

    if currency_response and oil_response:

        all_data['currency_rates'] = parse_currency_data(currency_response.text)

        all_data['oil_prices'] = parse_oil_data(oil_response.text)

        all_data['bitcoin_price'] = round(float(get_bitcoin_price()), 2)

        cities = ['Київ', 'Одеса', 'Львів', 'Дніпро']
        all_data['weather'] = {city: get_weather(city, weather_api) for city in cities}

        all_data['today_date'] = today_date_str

        days_ua = ['ПОНЕДІЛОК', 'ВІВТОРОК', 'СЕРЕДА', 'ЧЕТВЕР', 'П’ЯТНИЦЯ', 'СУБОТА', 'НЕДІЛЯ']
        day_of_week = days_ua[datetime.now().weekday()]
        all_data['day_of_week'] = day_of_week

    else:
        print("Не вдалося отримати дані")

    return all_data


print(get_all_data())