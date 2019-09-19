import telebot
token = '901123375:AAEkqavK06oVLcG517dG1Vl_TPRqV-a2-zA'

bot = telebot.TeleBot(token)


@bot.message_handler()
def hellower(message):
	bot.send_message(message.chat.id, 'Hello')
  
  
bot.polling()