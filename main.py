import json
import telebot
import requests

open_weather_token = 'a4f5f49533e6570aa7045c937b243151'
token = '5868468005:AAHoWglbRfawzNGufvA3mJ1xtr0-PX4j8GM'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def helloMessage(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = telebot.types.KeyboardButton('Минск')
    button1 = telebot.types.KeyboardButton('Москва')
    button2 = telebot.types.KeyboardButton('Ялта')
    markup.add(button)
    markup.add(button1)
    markup.add(button2)

    bot.send_message(message.chat.id, 'Привет! Выбери город и я пришлю тебе сводку погоды!', reply_markup=markup)

@bot.message_handler(content_types='text')
def text(message):
    if message.text == 'Минск' or message.text == 'Москва' or message.text == 'Ялта':
        res = getWeather(message.text)
        bot.send_message(message.chat.id, res)
    else:
        bot.send_message(message.chat.id, 'Я так не умею')


def getWeather(cur):
    response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric')
    data = json.loads(response.text)
    return data['Cur_OfficialRate']

bot.polling()