from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Solicitud de clave API al servicio de conversión de divisas:
API_KEY = "d44572aa3a61edda7d06284a"  # Reemplaza con tu clave real
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/"


@app.route('/convert', methods=['GET'])
def convert_currency():
    base_currency = request.args.get('from')
    target_currency = request.args.get('to')
    amount = request.args.get('amount', type=float)

    if not base_currency or not target_currency or amount is None:
        return jsonify({"error": "Missing parameters. Required: from, to, amount"}), 400

    response = requests.get(BASE_URL + base_currency)
    if response.status_code != 200:
        return jsonify({"error": "Error fetching exchange rates"}), 500

    data = response.json()
    if target_currency not in data['conversion_rates']:
        return jsonify({"error": "Invalid target currency"}), 400

    exchange_rate = data['conversion_rates'][target_currency]
    converted_amount = amount * exchange_rate

    return jsonify({
        "base_currency": base_currency,
        "target_currency": target_currency,
        "exchange_rate": exchange_rate,
        "amount": amount,
        "converted_amount": converted_amount
    })


if __name__ == '__main__':
    app.run(debug=True)
