from AbstractAPI import AbstractAPI, APIError
import os
from dotenv import load_dotenv

load_dotenv()

GPT_BASE_URL = 'https://api.openai.com'
GPT_API_KEY = os.getenv('GPT_API_KEY')

class SentimentAPIError(APIError):
  def __init__(self, message):
    self.message = message

class SentimentAPI(AbstractAPI):
  model = ""
  role = ""
  temp = 0

  header = {
    "Authorization": f"Bearer {GPT_API_KEY}",
    "Content-Type": "application/json",
  }

  def _create_data(self, content, model="", role="", temp=0):
    if not model:
      model = self.model
    if not role:
      role = self.role
    if not temp:
      temp = self.temp

    return {
      "model": model,
      "messages": [{"role": role, "content": content}],
      "temperature": temp
    }

  def __init__(self, model="gpt-4o", role="user", temp=0.7):
    super().__init__(GPT_BASE_URL, GPT_API_KEY)
    self.model = model
    self.role = role
    self.temp = temp

  def _test(self):
    test_data = self._create_data("Say this is a test!")
    print(test_data)
    input()

    response = self.post(endpoint='/v1/chat/completions', 
                    data=test_data,
                    headers=self.header)

    if response.status_code != 200:
      raise SentimentAPIError(f"API returned status code {response.status_code}.\n{response.text}")

    return response.json()['choices'][0]['message']['content']

    

  def _get_response(self, content):
    data = self._create_data(content)
    response = self.post(endpoint='/v1/chat/completions', 
                    data=data,
                    headers=self.header)

    if response.status_code != 200:
      raise SentimentAPIError(f"API returned status code {response.status_code}.\n{response.text}")

    return response.json()['choices'][0]['message']['content']

  def get_coin_sentiment(self, coin):
    coin_name = coin.name
    coin_symbol = coin.symbol
    coin_url = f"https://pump.fun/coin/{coin.url}"

    message = f"Take a look at the cryptocurrency {coin_name} ({coin_symbol}) from {coin_url}. Rate it out of 10 based on its social media presence. Just provide the rating with no other text."

    return self._get_response(message)
# test
if __name__ == '__main__':
  sentimentAPI = SentimentAPI(model='gpt-4o')
  import CryptoAPI
  cryptoAPI = CryptoAPI.CryptoAPI()
  clist = cryptoAPI.get_coin_list()
  coin = clist[0]
  print(coin)
  response = sentimentAPI.get_coin_sentiment(coin)
  print(response)