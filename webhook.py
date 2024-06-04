from flask import Flask, request
import requests
import os
import re
app = Flask(__name__)


TELEGRAM_BOT_TOKEN = "7355318730:AAEOBVb3imL7Z3DByxlZuRgbm8--QQtPJXg"
TELEGRAM_CHAT_ID ="6082352981"

def send_telegram_message(message):
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
    data = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message
    }
    response = requests.post(url, data=data)
    return response.json()

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    description_match = re.search(r'- description = (.+)', data['message'])
    if description_match:
        description_match=description_match.group(0)
    else:
        description_match=" "
    summary_match = re.search(r'- summary = (.+)', data['message'])
    if summary_match:
        summary_match=summary_match.group(0)
    else:
        summary_match=" "
    message = f"Peringatan\n{summary_match}\n{description_match}"
    send_telegram_message(message)
    return "Alert received!", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  
