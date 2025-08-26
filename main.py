from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random

async def dice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    number = random.randint(1, 6)
    await update.message.reply_text(f'🎲 عدد تاس: {number}')

app = ApplicationBuilder().token("8448246147:AAFZAD6X052apELfjFBOxU5OjhVyspdUP5M").build()
app.add_handler(CommandHandler("dice", dice))

app.run_polling()
