import telebot
import random
import os
from datetime import datetime
from persiantools.jdatetime import JalaliDate

# گرفتن توکن از متغیر محیطی برای امنیت بیشتر
TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

# هندلر برای دستور /tas
@bot.message_handler(commands=['tas'])
def send_dice(message):
    chat_id = message.chat.id
    bot.send_dice(chat_id, emoji='🎲')
    dice_number = random.randint(1, 6)
    bot.send_message(chat_id, f"عدد تاس شما هست: {dice_number}")

# هندلر برای دستور /date
@bot.message_handler(commands=['date'])
def send_date(message):
    chat_id = message.chat.id
    today_gregorian = datetime.now().strftime("%Y-%m-%d")
    today_persian = JalaliDate.today().strftime("%Y/%m/%d")
    bot.send_message(chat_id, f"📅 تاریخ امروز:\nمیلادی: {today_gregorian}\nشمسی: {today_persian}")

# اجرای ربات
if __name__ == "__main__":
    bot.polling(none_stop=True)
