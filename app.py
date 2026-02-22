from flask import Flask, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

BOT_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

@app.route("/intruders", methods=["POST"])
def intruder():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": "intruder detected"
    }

    r = requests.post(url, data=payload)

    if r.status_code == 200:
        return {"status": "sent"}, 200
    else:
        return {"status": "error", "details": r.json()}, 500