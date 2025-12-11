import os
from dotenv import load_dotenv
import telebot

load_dotenv()
TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, message.text)

print("Launching bot...")
bot.infinity_polling()
