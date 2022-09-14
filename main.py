 import os
 import whtsappbot
 bot = whtsappbot.whtsapp.bot("sesson here")
   
@bot.message_hadller(comands=["alive"])
def send_welcome(message):
	bot.reply_to(message,"HI! I'm ALIVE Now")
	
@bot.message_handler(comands=[".menu"])
def send_message(message):
	bot.send_message(message["bot not  create"])
	
bot.polling()