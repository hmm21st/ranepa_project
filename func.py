import config as cfg
import telebot
import random

token=cfg.TOKEN
bot=telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.chat.id,'Привет👋🏻')

@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text.lower() in 'как дела?':
        bot.send_message(message.chat.id, random.choice(['Отлично!', 'Всё супер :)', 'Okey👌🏻']))
        
    elif message.text.lower() in ['hi', 'привет', 'салют']:
        bot.send_message(message.chat.id, 'Привет👋🏻')