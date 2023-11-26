import telebot
from telebot import types
from image_generator import generate_image

# Ваш токен, отриманий від BotFather
bot_token = '6328902020:AAHYKlkCtqCzcuy5asECY-Gw55FREpuZBJk'
bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Створюємо клавіатуру
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button_start = types.KeyboardButton('/start')
    button_get_image = types.KeyboardButton('/getimage')
    keyboard.add(button_start, button_get_image)

    # Відправляємо повідомлення разом із клавіатурою
    bot.send_message(message.chat.id, "Виберіть опцію:", reply_markup=keyboard)

@bot.message_handler(commands=['getimage'])
def send_image(message):
    # Створюємо клавіатуру
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button_start = types.KeyboardButton('/start')
    button_get_image = types.KeyboardButton('/getimage')
    keyboard.add(button_start, button_get_image)

    bot.send_message(message.chat.id, "Очікуйте, створюється картинка", reply_markup=keyboard)
    image_path = generate_image()
    with open(image_path, 'rb') as photo:
        bot.send_photo(message.chat.id, photo)

if __name__ == '__main__':
    bot.polling()
