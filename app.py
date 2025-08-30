from flask import Flask, request
import requests
import random
import os

TOKEN = os.environ.get("BOT_TOKEN")  # توکن رباتتو اینجا ست کن
URL = f"https://api.telegram.org/bot{TOKEN}"

app = Flask(__name__)

def send_message(chat_id, text):
    requests.post(f"{URL}/sendMessage", json={"chat_id": chat_id, "text": text})

def send_dice(chat_id):
    requests.post(f"{URL}/sendDice", json={"chat_id": chat_id, "emoji": "🎲"})

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        if "تاس" in text:
            # اول استیکر تاس رو می‌فرسته
            send_dice(chat_id)

            # بعد عدد رندوم بین 1 تا 6
            number = random.randint(1, 6)
            reply = f"عدد تاس شما هست: {number}\n\nگروه بچه های ایرون @iran9897"
            send_message(chat_id, reply)

    return "ok"

if __name__ == "__main__":
    app.run(port=5000)
