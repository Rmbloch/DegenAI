from flask import Flask, jsonify, render_template, make_response
from CryptoAPI import CryptoAPI
from SentimentAPI import SentimentAPI
import threading
import time
import random
import bisect
from flask_cors import CORS

app = Flask(__name__, template_folder='../templates')
CORS(app)

crypto_api = CryptoAPI()
sentiment_api = SentimentAPI()
coin_data = []

@app.route('/')
def serve_homepage():
    return render_template("index.html")

def refresh_data():
    global coin_data
    while True:
        print("Refreshing coin data...")
        # iterate through every coin
        try:
            coins = crypto_api.get_coin_list()
            # init all the sentiment scores to 0
            for coin in coins:
                coin.sentiment_score = 0
            
            # coins = coins[:5]
            for coin in coins:
                raw_sentiment_score = sentiment_api.get_coin_sentiment(coin)
                try:
                    coin.sentiment_score = raw_sentiment_score
                except (ValueError, TypeError):
                    coin.sentiment_score = 0
                print("Adding judged coin to list")
                coin_data.append(coin)
                coin_data.sort(key=lambda x: x.sentiment_score, reverse=True)
                
            print("Data refreshed.")
        except Exception as e:
            print(f"Error refreshing data: {e}")
        #time.sleep(10) # Uncomment this if you dont want to be able use the refresh button on the html.
        # When commented, data refreshes all the time. 

@app.route('/api/coins', methods=['GET'])
def get_top_coins():
    return jsonify([{
        "name": coin.name,
        "symbol": coin.symbol,
        "price": coin.price,
        "url": coin.url,
        "image_url": coin.image_url,
        "sentiment_score": getattr(coin, "sentiment_score", 0)
    } for coin in coin_data])

if __name__ == '__main__':
    threading.Thread(target=refresh_data, daemon=True).start()
    app.run(debug=True)