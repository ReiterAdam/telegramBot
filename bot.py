import os
import telebot

# for formula 1 api
import requests
import formula1

# import token and get bot
BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

# add message handler to start and Hello command
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Hello there!")

    
@bot.message_handler(commands=['drivers'])
def list_drivers(message):
    bot.reply_to(message, formula1.getListOfDrivers())

    
@bot.message_handler(commands=['schedule'])
def display_schhedule(message):
    bot.reply_to(message, formula1.getSchedules())
   

# any message will be echoed to user
# @bot.message_handler(func=lambda msg:True)
# def echo_all(message):
#     bot.reply_to(message, message.text)


# make it work
bot.infinity_polling()