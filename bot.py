import telebot
from image_generator import generate_image

# Ваш токен, отриманий від BotFather
bot_token = '6328902020:AAHYKlkCtqCzcuy5asECY-Gw55FREpuZBJk'
bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привіт! Надішліть команду /getimage, щоб отримати зображення.")

@bot.message_handler(commands=['getimage'])
def send_image(message):
    image_path = generate_image()
    with open(image_path, 'rb') as photo:
        bot.send_photo(message.chat.id, photo)

if __name__ == '__main__':
    bot.polling()
