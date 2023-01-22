import os
import telebot

# for formula 1 api
import requests
import formula1


# for trains schedule
import trains
import schedule
import time



# import token and get bot
BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)
user_id = '5902568309'




def scheduled_updates():
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
    
    bot.reply_to(message, "Powiadomienia wlaczone")    
    bot.reply_to(message, f'Aktualnie mamy:\n{trains.displayTrains()}')

    schedule.every().day.at("6:00").do(scheduled_updates)
    while True:
        schedule.run_pending()
        time.sleep(1)
 

@bot.message_handler(commands=['idontliketrains'])
def stop_updates(message):
#    sched.remove_job('scheduledUpdates')
    bot.reply_to(message, "Powiadomienia wylaczone")
    schedule.clear()
# any message will be echoed to user
# @bot.message_handler(func=lambda msg:True)
# def echo_all(message):
#     bot.reply_to(message, message.text)


# make it work
bot.infinity_polling()