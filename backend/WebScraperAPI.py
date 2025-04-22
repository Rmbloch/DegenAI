from AbstractAPI import AbstractAPI, APIError
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
import requests
import time
import Coin

# get keys
from dotenv import load_dotenv
import os
load_dotenv()
# get keys
SEARCH_KEY = os.getenv('SEARCH_KEY')
CSE_ID = os.getenv('CSE_ID')

class WebScraperAPIError(APIError):
  def __init__(self, message):
    self.message = message

class WebScraperAPI(AbstractAPI):
  def __init__(self):
    super().__init__(base_url="", api_key=None)  # No API key needed for local browser scraping
    self.driver = self.init_webdriver()


  def init_webdriver(self):
    options = Options()
    options.add_argument("--headless")  # Run Chrome in headless mode
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument(
      "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
      "AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/122.0.0.0 Safari/537.36"
    )
    return webdriver.Chrome(options=options)

  def fetch_bs4_text(self, url, max_length=2000):
    try:
      response = requests.get(url)
      response.raise_for_status()
      soup = BeautifulSoup(response.text, "html.parser")
      text = soup.get_text(separator="\n", strip=True)
      return text[:max_length]
    except requests.RequestException as e:
      raise WebScraperAPIError(f"Requests error fetching {url}: {e}")
    except Exception as e:
      raise WebScraperAPIError(f"Unexpected error fetching {url}: {e}")

  def fetch_page_text(self, url, max_length=2000, wait_time=0):
    try:
      self.driver.get(url)
      time.sleep(wait_time)  # Wait for JS to render (adjust as needed)

      page_source = self.driver.page_source
      soup = BeautifulSoup(page_source, "html.parser")
      text = soup.get_text(separator="\n", strip=True)
      return text[:max_length]

    except WebDriverException as e:
      raise WebScraperAPIError(f"Selenium error fetching {url}: {e}")
    except Exception as e:
      raise WebScraperAPIError(f"Unexpected error fetching {url}: {e}")
    finally:
      try:
        self.driver.quit()
      except:
        pass
  
  def get_links(self, coin: Coin, num_results=5):
    crypto_name = coin.name
    query = f"\"{crypto_name}\" cryptocurrency news"
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
      "key": SEARCH_KEY,
      "cx": CSE_ID,
      "q": query,
      "num": num_results
    }

    try:
      response = requests.get(url, params=params)
      response.raise_for_status()
      data = response.json()
      links = [item["link"] for item in data.get("items", [])]
      return links
    except Exception as e:
      print(f"Search failed: {e}")
      return [] 

if __name__ == "__main__":
  web_scraper_api = WebScraperAPI()
  import CryptoAPI
  crypto_api = CryptoAPI.CryptoAPI()
  coin_list = crypto_api.get_coin_list()
  coin = coin_list[0]

  links = web_scraper_api.get_links(coin)
  print(len(links))
  for link in links:
    print(f"-- {link}")
    page_data = web_scraper_api.fetch_page_text(link, max_length=8000)
    print(page_data)
    input()