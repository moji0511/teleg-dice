import random
import telebot
import os

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['tas'])
def send_dice(message):
    bot.send_dice(message.chat.id, emoji='🎲')
    dice_number = random.randint(1, 6)
    bot.send_message(message.chat.id, f"عدد تاس شما هست: {dice_number}")

bot.infinity_polling()
