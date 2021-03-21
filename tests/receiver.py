from datetime import datetime

import requests
import time


def pretty_messages(message):
    dt = datetime.fromtimestamp(message['time'])
    dt_str = dt.strftime('%H:%M:%S')
    print(message['name'], dt_str)
    print(message['text'])
    print()


after = 0.0
while True:
    # Получаем новое сообщение
    data = requests.get('http://127.0.0.1:5000/messages', params={'after': after}).json()
    for message in data['messages']:
        pretty_messages(message)
        after = message['time']
    time.sleep(1)
