from flask import Flask, request
import requests
import random
import os

app = Flask(__name__)

TOKEN = "8206388608:AAFAHSviQ0gyW7dbEmm0JHv6aiJHtDPrrIA"
TELEGRAM_API = f"https://api.telegram.org/bot{TOKEN}"

# وبهوک ربات
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    if not data or "message" not in data:
        return {"ok": True}

    chat_id = data["message"]["chat"]["id"]
    text = data["message"].get("text", "")

    if "تاس" in text:
        number = random.randint(1, 6)

        # ارسال استیکر تاس (ایموجی 🎲 واقعی تلگرام)
        requests.post(f"{TELEGRAM_API}/sendDice", json={"chat_id": chat_id})

        # ارسال متن نتیجه
        reply = f"🎲 عدد تاس شما هست: {number}\n\nگروه بچه های ایرون @iran9897"
        requests.post(f"{TELEGRAM_API}/sendMessage", json={"chat_id": chat_id, "text": reply})

    return {"ok": True}

@app.route('/')
def home():
    return "Dice Bot is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
