import json
import telebot
import requests

token = '5868468005:AAHoWglbRfawzNGufvA3mJ1xtr0-PX4j8GM'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def helloMessage(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = telebot.types.KeyboardButton('Минск')
    button1 = telebot.types.KeyboardButton('Нарочь')
    button2 = telebot.types.KeyboardButton('Ялта')
    button3 = telebot.types.KeyboardButton('Санкт-Петербург')
    button4 = telebot.types.KeyboardButton('Москва')
    markup.add(button)
    markup.add(button1)
    markup.add(button2)
    markup.add(button3)
    markup.add(button4)

    bot.send_message(message.chat.id, 'Привет! Погода в городе:', reply_markup=markup)

@bot.message_handler(content_types='text')
def text(message):
    if message.text == 'USD' or message.text == 'EUR' or message.text == 'CNY':
        res = getCourse(message.text)
        bot.send_message(message.chat.id, res)
    else:
        bot.send_message(message.chat.id, 'Я так не умею')


def getCourse(cur):
    response = requests.get('https://www.nbrb.by/api/exrates/rates/'+cur+'?parammode=2')
    data = json.loads(response.text)
    return data['Cur_OfficialRate']

bot.polling()