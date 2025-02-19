from AbstractAPI import AbstractAPI
from dotenv import load_dotenv
import os

load_dotenv()

CRYPTO_API_BASE_URL = 'https://utvegumaxuxnpmzzmimk.supabase.co/'
CRYPTO_API_KEY = os.getenv('CRYPTO_API_KEY')

""" options:
limit=10&order=created_time.desc&select=*&bonding_curve_completed=is.true
"""

class CryptoAPI(AbstractAPI):
  token_endpoint = 'rest/v1/tokens'
  headers = {
    "apikey": CRYPTO_API_KEY,
  }
  coin_list_params = {
    "limit": 10,
    "order": "created_time.desc", 
    "select": "*", 
    "bonding_curve_completed": "is.true"
  }

  def __init__(self):
    super().__init__(CRYPTO_API_BASE_URL, CRYPTO_API_KEY)

  def get_coin_list(self):
    return self.get(endpoint=self.token_endpoint, 
                    params=self.coin_list_params,
                    headers=self.headers)