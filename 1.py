import telebot
import requests

token = '901123375:AAEkqavK06oVLcG517dG1Vl_TPRqV-a2-zA'
bot = telebot.TeleBot(token)


@bot.message_handler(commands = ['start'])
def helower(message):
    button = telebot.types.ReplyKeyboardMarkup()
    button.row('Отримати курс валюти')
    button.row('Знайти найближчий банкомат')

    bot.send_message(message.chat.id, "Привіт, Вас вітає наш бот. Введіть повідомлення:", reply_markup =button )

'''@bot.message_handler(content_types = ['text'])
def helower(message):
    bot.send_message(message.chat.id, message.text)'''

@bot.message_handler(func = lambda s: s.text == "Отримати курс валюти" , content_types = ['text'])
def helower(message):
    menu = telebot.types.InlineKeyboardMarkup()
    button1 = telebot.types.InlineKeyboardButton(text = "EUR" , callback_data = 'EUR' )
    button2 = telebot.types.InlineKeyboardButton(text = "USD" , callback_data = 'USD' )
    menu.add(button1, button2)
    bot.send_message(message.chat.id, "Виберіть валюту", reply_markup =menu )

@bot.callback_query_handler(func = lambda call: call.data == 'EUR')
def eurower(call):
    par = {'valcode' : 'EUR'}
    r = requests.get('https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?json', params=par, verify=False).json()


    bot.send_message(call.message.chat.id, str(r[0]['rate']))


@bot.callback_query_handler(func = lambda call: call.data == 'USD')
def eurower(call):
    global val
    val = 25
    bot.send_message(call.message.chat.id, "Курс валюти 25 грн за долар. ВВедіть суму" )





@bot.message_handler(content_types = ['location'])
def helower(message):
    lat = message.location.latitude
    bot.send_message(message.chat.id, lat)


bot.polling()