from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import time
from threading import Thread, Event

app = Flask(__name__)
CORS(app)  # Enable CORS

API_ENDPOINTS = [
    "https://rnf.nsmodz.top/api.php?phone=",
    "http://168.119.39.20/~rnfmodsc/api/69.php?phone=",
    # Add other endpoints here
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
            except Exception ase:
                print(f"Error contacting {api}: {e}")
        time.sleep(1)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
