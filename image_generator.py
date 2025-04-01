from PIL import Image, ImageDraw, ImageFont
from data_fetcher import get_all_data, get_weather_iconid
import requests
from io import BytesIO


def generate_image():

    weather_api = "58c4b2e9a9b2565b6ab85e8afb62527a"

    # Завантажте шрифт (необхідно вказати шлях до .ttf файлу шрифту)
    font_path = "Roboto/Roboto-Bold.ttf"  # або шлях до іншого файлу шрифту, який ви хочете використовувати
    try:
        font = ImageFont.truetype(font_path, size=30)
    except IOError:
        font = ImageFont.load_default()
        print("Не вдалося завантажити шрифт. Використовується шрифт за замовчуванням.")


    # Відкрийте картинку-шаблон
    template_image_path = "template.png"
    img = Image.open(template_image_path)
    draw = ImageDraw.Draw(img)


    # Функція для додавання тексту на картинку
    def draw_text(draw, text, position, font_path, font_size, color):
        try:
            font = ImageFont.truetype(font_path, size=font_size)
        except IOError:
            print(f"Не вдалося завантажити шрифт з {font_path}. Використовується шрифт за замовчуванням.")
            font = ImageFont.load_default()
        draw.text(position, text, font=font, fill=color)

    data = get_all_data()
    font_size = 30

    # Координати для тексту (ви повинні визначити ці координати для вашої картинки)
    coordinates = {
        'usd_buy': (670, 145),
        'usd_sell': (805, 145),
        'eur_buy': (670, 200),
        'eur_sell': (805, 200),
        'btc': (730, 255),
        'A95': (310, 330),
        'diesel': (310, 380),
        'gas': (310, 430),
        'Kyiv_weather': (490, 550),
        'Odesa_weather': (600, 550),
        'Lviv_weather': (710, 550),
        'Dnipro_weather': (825, 550),
        'today_date': (150, 500),
        'day_of_week': (150, 550)
    }

    colors = {
        'currency_rates': "white",
        'oil_prices': "white",
        'bitcoin_price': "white",
        'weather': "white",
        'today_date': "white",
        'day_of_week': "white"
    }

    draw_text(draw, f"{data['currency_rates']['usd']['buy']}", coordinates['usd_buy'], font_path, font_size, colors['currency_rates'])
    draw_text(draw, f"{data['currency_rates']['usd']['sell']}", coordinates['usd_sell'], font_path, font_size, colors['currency_rates'])
    draw_text(draw, f"{data['currency_rates']['eur']['buy']}", coordinates['eur_buy'], font_path, font_size, colors['currency_rates'])
    draw_text(draw, f"{data['currency_rates']['eur']['sell']}", coordinates['eur_sell'], font_path, font_size, colors['currency_rates'])
    draw_text(draw, f"{data['bitcoin_price']}", coordinates['btc'], font_path, font_size, colors['bitcoin_price'])
    draw_text(draw, f"{data['oil_prices']['A95']}", coordinates['A95'], font_path, font_size, colors['oil_prices'])
    draw_text(draw, f"{data['oil_prices']['diesel']}", coordinates['diesel'], font_path, font_size, colors['oil_prices'])
    draw_text(draw, f"{data['oil_prices']['gas']}", coordinates['gas'], font_path, font_size, colors['oil_prices'])
    draw_text(draw, data['weather']['Київ'], coordinates['Kyiv_weather'], font_path, font_size, colors['weather'])
    draw_text(draw, data['weather']['Одеса'], coordinates['Odesa_weather'], font_path, font_size, colors['weather'])
    draw_text(draw, data['weather']['Львів'], coordinates['Lviv_weather'], font_path, font_size, colors['weather'])
    draw_text(draw, data['weather']['Дніпро'], coordinates['Dnipro_weather'], font_path, font_size, colors['weather'])
    draw_text(draw, data['today_date'], coordinates['today_date'], font_path, 50, '#193872')
    draw_text(draw, data['day_of_week'], coordinates['day_of_week'], font_path, font_size, 'black')


    def download_weather_icon(icon_id):
        icon_url = f"http://openweathermap.org/img/wn/{icon_id}@2x.png"
        response = requests.get(icon_url)
        if response.status_code == 200:
            icon = Image.open(BytesIO(response.content))
            # Отримання поточних розмірів іконки
            current_width, current_height = icon.size
            # Розрахунок нових розмірів (збільшення на 50%)
            new_size = (int(current_width * 1.3), int(current_height * 1.3))
            # Зміна розмірів іконки
            icon = icon.resize(new_size)
            return icon
        else:
            print(f"Не вдалося завантажити іконку: {icon_id}")
            return None


    cities_weather = {}
    for city in ['Київ', 'Одеса', 'Львів', 'Дніпро']:
        icon_id = get_weather_iconid(city, weather_api)
        if icon_id:
            cities_weather[city] = {
                'icon': download_weather_icon(icon_id)
            }

    # Позиції для іконок на картинці
    icon_positions = {
        'Київ': (450, 420),
        'Одеса': (560, 420),
        'Львів': (670, 420),
        'Дніпро': (780, 420)
    }

    # Додавання іконок погоди на основне зображення
    for city, weather in cities_weather.items():
        if weather['icon']:
            img.paste(weather['icon'], icon_positions[city], weather['icon'])


    # Збережіть результат
    output_image_path = "ready.png"
    img.save(output_image_path)

    return 'ready.png'

generate_image()
