from collections import defaultdict
import telebot
import requests


token = '901123375:AAEkqavK06oVLcG517dG1Vl_TPRqV-a2-zA'
bot = telebot.TeleBot(token)


Level1, Level2, Level3, Level4 = range(4)

level_dict = defaultdict(lambda : Level1)
order_dict = defaultdict(lambda: {})

def update_order(message, param):
    order_dict[message.chat.id][param] = message.text

def get_order(chat_id):
    print(order_dict[chat_id])
    return order_dict[chat_id]

def update_lvl(message, level):
    level_dict[message.chat.id] = level

def get_lvl(message):
    return level_dict[message.chat.id]


@bot.message_handler(commands=['start'])
def handle_text(message):
    user_markup = telebot.types.ReplyKeyboardMarkup()
    user_markup.row('Знайти', 'Замовити розвязок')
    user_markup.row('Формули')
    user_markup.row('Наш сайт')
    bot.send_message(message.chat.id, "Привіт", reply_markup=user_markup)

@bot.message_handler(func = lambda mess: mess.text =='Знайти' and get_lvl(mess) == Level1, content_types=['text'] )
def handle_text(message):
    update_lvl(message,Level2)
    bot.send_message(message.chat.id, "Введіть своє імя")


@bot.message_handler(func  = lambda mess: get_lvl(mess) == Level2, content_types=['text'] )
def handle_text(message):
    update_order(message, 'name')
    update_lvl(message,Level3)
    bot.send_message(message.chat.id, "ВВедіть свій вік:")

@bot.message_handler(func  = lambda mess: get_lvl(mess) == Level3, content_types=['text'] )
def handle_text(message):
    update_lvl(message,Level4)
    update_order(message, 'age')
    bot.send_message(message.chat.id, "Введіть ціну")

@bot.message_handler(func  = lambda mess: get_lvl(mess) == Level4, content_types=['text'] )
def handle_text(message):
    update_order(message, 'price')
    del level_dict[message.chat.id]
    helper_dict = get_order(message.chat.id)
    bot.send_message(message.chat.id, f"Ваша заявка прийнята, {helper_dict['name']}. Очікуйте")
    get_order(message.chat.id)


@bot.message_handler(func = lambda mess: mess.text =='Формули' and get_lvl(mess) == Level1, content_types=['text'] )
def handle_text(message):
	markup = telebot.types.InlineKeyboardMarkup()
	button = telebot.types.InlineKeyboardButton(text='Скорочене множення', callback_data='#001')
	button1 = telebot.types.InlineKeyboardButton(text='Ще щось', callback_data='#002')
	markup.add(button, button1)
	bot.send_message(message.chat.id, 'Виберіть із списку:', reply_markup=markup)
	
@bot.callback_query_handler(func=lambda call: call.data == '#001')
def query_handler(call):
	
	f= open('1.png', 'rb')
	photo = f.read()
	f.close()
    chat_id=call.message.chat.id
	
'''@bot.message_handler(..., content_types=['text'] )
def handle_lvl(message):







@bot.callback_query_handler(func=lambda call: call.data == )
def query_handler(call):
    chat_id=call.message.chat.id'''


'''
ТУТ кнопки
markup = telebot.types.InlineKeyboardMarkup()
button = telebot.types.InlineKeyboardButton(text='Скорочене множення', callback_data='#001')
button1 = telebot.types.InlineKeyboardButton(text='Ще щось', callback_data='#002')
markup.add(button, button1)
bot.send_message(message.chat.id, 'Виберіть із списку:', reply_markup=markup)
'''






bot.polling(none_stop=True)
