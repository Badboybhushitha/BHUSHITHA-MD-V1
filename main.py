import os
import telebot

bot = telebot.TeleBot("5482082877:AAFQWywdiKFolCw_bSnzjL3g9SEoE9_oZeQ")

@bot.message_handler(comands=["start"])
def send_welcome(message):
    bot.reply_to(message,"HELLO")

    @bot.message_handler(comands=["how"])
    def send_message(message):
        bot.send_message(message, "http:wa.me/94742427578")

    bot.polling()
