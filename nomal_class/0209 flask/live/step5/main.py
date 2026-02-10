from flask import Flask, render_template
from flask_sock import Sock
import requests

app = Flask(__name__)
sock = Sock(app)

@app.route("/")
def index():
    return render_template("btc.html")

@sock.route("/ws")
def websocket(ws):
    while True:
        url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
        result = requests.get(url).json()
        price = result["price"]

        # {
        #   "symbol": "BTCUSDT",
        #   "price": "70529.40000000"
        # }
        ws.send(price)

if __name__ == "__main__":
    app.run(debug=True)