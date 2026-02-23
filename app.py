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

    data = request.get_json()
    print("data received from ESP: ", data)
    
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": "intruder detected"
    }

    r = requests.post(url, json=payload)

    print("Status code:", r.status_code)
    print("Response text:", r.text)

    return {"telegram_status": r.status_code, "response": r.text}, 200