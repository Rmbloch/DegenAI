from flask import Flask, jsonify, render_template, make_response
from flask_cors import CORS
from CryptoAPI import CryptoAPI
from SentimentAPI import SentimentAPI
import threading
import time
import random

app = Flask(__name__, template_folder='../templates')
CORS(app)

crypto_api = CryptoAPI()
sentiment_api = SentimentAPI()
coin_data = []

def refresh_data():
    global coin_data
    while True:
        print("Refreshing coin data...")
        try:
            coins = crypto_api.get_coin_list()
            coins = coins[:5]
            for coin in coins:
                print(coin.name)
                coin.sentiment_score = sentiment_api.get_coin_sentiment(coin)
            coin_data = sorted(coins, key=lambda x: getattr(x, "sentiment_score", 0), reverse=True)[:5]
            print("Data refreshed.")
        except Exception as e:
            print(f"Error refreshing data: {e}")
        time.sleep(5)

@app.route('/api/coins', methods=['GET'])
def get_top_coins():
    return jsonify([{
        "name": coin.name,
        "symbol": coin.symbol,
        "price": coin.price,
        "url": coin.url,
        "sentiment_score": getattr(coin, "sentiment_score", 0)
    } for coin in coin_data])

if __name__ == '__main__':
    threading.Thread(target=refresh_data, daemon=True).start()
    app.run()