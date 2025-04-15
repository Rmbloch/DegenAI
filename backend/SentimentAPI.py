import WebScraperAPI
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
  web_scraper_api = None

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

  def __init__(self, model="gpt-4o-mini", role="user", temp=0.7):
    super().__init__(GPT_BASE_URL, GPT_API_KEY)
    self.model = model
    self.role = role
    self.temp = temp
    self.web_scraper_api = WebScraperAPI.WebScraperAPI()

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

  def _fetch_page_text(self, url, max_length=8000):
    # return self.web_scraper_api.fetch_page_text(url, max_length=max_length)
    return self.web_scraper_api.fetch_page_text(url, max_length=max_length, wait_time=1)

  def get_coin_sentiment(self, coin):
    coin_name = coin.name
    coin_symbol = coin.symbol
    coin_url = f"https://pump.fun/coin/{coin.url}"

    # Fetch the page text
    page_data = self._fetch_page_text(coin_url)

    # Fetch links
    links = self.web_scraper_api.get_links(coin)

    # Get link data
    for link in links:
      page_data += "\n\n"
      page_data += self._fetch_page_text(link)

    # message = f"Take a look at the cryptocurrency {coin_name} ({coin_symbol}). Rate it out of 10 based on its social media presence. Just provide the rating with no other text. The page text is as follows:\n\n{page_data}\n\n"
    message = f"Take a look at the cryptocurrency {coin_name} ({coin_symbol}). Rate it from 0 to 9 based on its online. Just provide the rating with no other text. The page text is as follows:\n\n{page_data}"

    return self._get_response(message)
# test
if __name__ == '__main__':
  sentimentAPI = SentimentAPI(model='gpt-4o')
  import CryptoAPI
  cryptoAPI = CryptoAPI.CryptoAPI()
  clist = cryptoAPI.get_coin_list()
  coin = clist[0]

  coin_url = f"https://pump.fun/coin/{coin.url}"
  page_data = sentimentAPI._fetch_page_text(coin_url)
  # print(page_data)

  get_sentiment = sentimentAPI.get_coin_sentiment(coin)
  print(get_sentiment)