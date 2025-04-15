from AbstractAPI import AbstractAPI, APIError
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
import time

class WebScraperAPIError(APIError):
  def __init__(self, message):
    self.message = message

class WebScraperAPI(AbstractAPI):
  def __init__(self):
    super().__init__(base_url="", api_key=None)  # No API key needed for local browser scraping

  def fetch_page_text(self, url, max_length=2000, wait_time=5):
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

    try:
      driver = webdriver.Chrome(options=options)
      driver.get(url)
      time.sleep(wait_time)  # Wait for JS to render (adjust as needed)

      page_source = driver.page_source
      soup = BeautifulSoup(page_source, "html.parser")
      text = soup.get_text(separator="\n", strip=True)
      return text[:max_length]

    except WebDriverException as e:
      raise WebScraperAPIError(f"Selenium error fetching {url}: {e}")
    except Exception as e:
      raise WebScraperAPIError(f"Unexpected error fetching {url}: {e}")
    finally:
      try:
        driver.quit()
      except:
        pass
