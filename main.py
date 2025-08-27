import random
import telebot
import os

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['tas'])
def send_dice(message):
    # ارسال استیکر تاس
    bot.send_dice(message.chat.id, emoji='🎲')
    
    # تولید عدد تصادفی بین ۱ تا ۶
    dice_number = random.randint(1, 6)
    
    # ارسال پیام عدد تاس
    bot.send_message(message.chat.id, f"عدد تاس شما هست: {dice_number}")

# اجرای ربات به صورت polling
bot.infinity_polling()
