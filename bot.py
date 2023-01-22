import os
import telebot

# for formula 1 api
import requests
import formula1


# for trains schedule
import trains
from telegram.ext import Updater



# import token and get bot
BOT_TOKEN = os.environ.get('BOT_TOKEN')
u = Updater(BOT_TOKEN, asyncio.Queue)
bot = telebot.TeleBot(BOT_TOKEN)
user_id = '5902568309'


j = u.job_queue

def scheduled_updates(context: telegram.ext.CallbackContext):
    bot.send_message(user_id, trains.displayTrains())

# add message handler to start and Hello command
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Hello there!")

    
@bot.message_handler(commands=['f1drivers'])
def list_drivers(message):
    bot.reply_to(message, formula1.getListOfDrivers())

    
@bot.message_handler(commands=['f1schedule'])
def display_schhedule(message):
    bot.reply_to(message, formula1.getSchedules())
   
@bot.message_handler(commands=['help','h'])
def display_schhedule(message):
    listOfCommands = "/start, /hello - welcome message\n/f1drivers - list of current drivers\n/f1schedule - schedule for this year"
    bot.reply_to(message, listOfCommands)
    
@bot.message_handler(commands=['iliketrains'])
def start_updates(message):
    #sched.add_job(scheduled_updates, trigger="cron", hour = 1, id='scheduledUpdates')
    #sched.add_job(scheduled_updates, 'interval', minutes = 1, id='scheduledUpdates')
#    chat_id = message[-1].chat.id
    job = j.run_repeating(scheduled_updates, interval=20, first=20)
    bot.send_message(user_id, "Powiadomienia wlaczone")
    bot.send_message(user_id, f'Aktualnie mamy:\n{trains.displayTrains()}')

@bot.message_handler(commands=['idontliketrains'])
def stop_updates(message):
#    sched.remove_job('scheduledUpdates')
    bot.send_message(user_id, "Powiadomienia wylaczone")
    
# any message will be echoed to user
# @bot.message_handler(func=lambda msg:True)
# def echo_all(message):
#     bot.reply_to(message, message.text)


# make it work
bot.infinity_polling()