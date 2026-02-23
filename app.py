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

    if not BOT_TOKEN or not CHAT_ID:
        return {"status": "error", "details": "bot token or chat_id not found"}, 500

    data = request.get_json()
    if not data or "message" not in data:
        print("returning 400: no message")
        return {"status": "error", "details": "no message"}, 400
    else:
        print("data received from ESP: ", data)

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": "intruder detected"
    }

    r = requests.post(url, json=payload, timeout=5)

    print("Status code:", r.status_code)
    print("Response text:", r.text)

    if r.status_code != 200:
        return {"telegram_status": r.status_code}, 500
    else:
        return {"telegram_status": r.status_code, "response": r.text}, 200