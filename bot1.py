import telebot
token = '901123375:AAEkqavK06oVLcG517dG1Vl_TPRqV-a2-zA'

bot = telebot.TeleBot(token)


@bot.message_handler(command = ['start'])
def hellower(message):
	button = telebot.types.ReplyKeyboardMarkup()
	button.row('Кнопка 1')
	button.row('Кнопка 2')
	
	
	bot.send_message(message.chat.id, 'Привіт, Вас вітає бот.Введіть повідомлення:', reply_markup = button)
  
@bot.message_handler(content_types = ['text'])
def hellower(message):
	bot.send_message(message.chat.id, message.text)  
	
	
@bot.message_handler(content_types = ['location'])
def hellower(message):
	bot.send_message(message.chat.id, message.location)




	
bot.polling()