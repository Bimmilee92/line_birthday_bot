import os
import json
import requests
from datetime import datetime

def send_line_message(user_id, message):
    headers = {
        'Authorization': f"Bearer {os.getenv('CHANNEL_ACCESS_TOKEN')}",
        'Content-Type': 'application/json'
    }
    data = {
        "to": user_id,
        "messages": [{
            "type": "text",
            "text": message
        }]
    }
    res = requests.post('https://api.line.me/v2/bot/message/push', headers=headers, json=data)
    print(f"Push result to {user_id}:", res.status_code, res.text)

def check_and_send_birthday():
    birthday_data = json.loads(os.getenv('BIRTHDAY_JSON', '{}'))
    today = datetime.now().strftime('%m-%d')

    for name, info in birthday_data.items():
        if info['date'] == today:
            msg = f"🎂 今天是{name}的生日，記得祝他生日快樂！"
            send_line_message(info['userId'], msg)

if __name__ == "__main__":
    check_and_send_birthday()
