import json
from AbstractAPI import AbstractAPI, APIError
from Coin import Coin
from dotenv import load_dotenv
import os

load_dotenv()

CRYPTO_API_BASE_URL = 'https://utvegumaxuxnpmzzmimk.supabase.co/'
CRYPTO_API_KEY = os.getenv('CRYPTO_API_KEY')

class CryptoAPIError(APIError):
  def __init__(self, message):
    self.message = message

class CryptoAPI(AbstractAPI):
  token_endpoint = 'rest/v1/tokens'
  headers = {
    "apikey": CRYPTO_API_KEY,
  }
  coin_list_params = {
    "limit": 20,
    "order": "created_time.desc", 
    "select": "*", 
    "bonding_curve_completed": "is.true"
  }

  def __init__(self):
    super().__init__(CRYPTO_API_BASE_URL, CRYPTO_API_KEY)

  # input: list of coin objects
  # output: list of unique coin objects
  def _filter_coins(self, coin_list):
    return list(set(coin_list))

  # input: list of coins in JSON from API
  # output: list of coin objects
  def _get_coin_objects(self, coin_list):
    coin_lambda = lambda coin: Coin(coin['name'], coin['symbol'], coin['price_in_usd'], coin['address'])
    coin_object_list = [coin_lambda(coin) for coin in coin_list]
    return self._filter_coins(coin_object_list)

  def get_coin_list(self):
    response = self.get(endpoint=self.token_endpoint, 
                    params=self.coin_list_params,
                    headers=self.headers)

    if response.status_code != 200:
      raise CryptoAPIError(f"API returned status code {response.status_code}.\n{response.text}")

    coin_list = response.json()
    
    return self._get_coin_objects(coin_list) 