from flask import Flask, request, Response
import time
from datetime import datetime, timezone

app = Flask(__name__)

messages = [
    # {'name': 'Mary', 'time': time.time(), 'text': 'Привет'},
    # {'name': 'Nick', 'time': time.time(), 'text': 'Привет!'},
]


@app.route("/send", methods=['POST'])
def send():
    # Получаю имя и текст из json
    name = request.json.get('name')
    text = request.json.get('text')
    # Проверяю, что name и text являются строковыми данными
    if not name or not isinstance(name, str) or not text or not isinstance(text, str):
        return Response(status=400)
    # Создаю сообщение с параметрами: имя, время, текст
    message = {'name': name, 'time': time.time(), 'text': text}
    # Добавляю в словарь
    messages.append(message)
    return Response(status=200)


"""
@app.route("/send", methods=['POST'])
def send():
    data = request.json
    if not isinstance(data, dict):
        return Response('not json', 404)

    text = data.get('text')
    name = data.get('name')

    if isinstance(text, str) and isinstance(name, str):
        messages.append({
            'name': name,
            'time': time.time(),
            'text': text
        })
        return Response("OK")
    else:
        return Response("wrong format", 400)"""


def filter_by_key(elements, key, threshold):
    filtered_elements = []

    for element in elements:
        if element[key] > threshold:
            filtered_elements.append(element)

    return filtered_elements


@app.route("/messages")
def messages_view():
    try:
        # Получаю новое время
        after = float(request.args['after'])
    except:
        return Response(status=400)
    # Фильтрую по ключу
    filtered = filter_by_key(messages, key='time', threshold=after)
    return {'messages': filtered}


@app.route("/")
def hello():
    return "Hello, World! <a href='/status'>Статус</a>"


@app.route("/status")
def status():
    return {
        'status': True,
        'name': 'Yaris',
        'time': time.time(),
        'time1': time.asctime(),
        'time2': datetime.now(),
        'time3': datetime.now().isoformat(),
        'time4': datetime.now(tz=timezone.utc).isoformat(),
        'time5': datetime.now().strftime('%Y-%m-%d'),
        'time6': datetime.now().strftime('%H%M%S %Y/%m/%d !')
    }


app.run()
