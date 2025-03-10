from AbstractAPI import AbstractAPI, APIError
import os
from dotenv import load_dotenv

load_dotenv()

GPT_BASE_URL = 'https://api.openai.com'
GPT_API_KEY = os.getenv('GPT_API_KEY')

# Authorization: Bearer OPENAI_API_KEY
# curl https://api.openai.com/v1/chat/completions \
#   -H "Content-Type: application/json" \
#   -H "Authorization: Bearer $OPENAI_API_KEY" \
#   -d '{
#      "model": "gpt-4o-mini",
#      "messages": [{"role": "user", "content": "Say this is a test!"}],
#      "temperature": 0.7
#    }'

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

  def create_data(self, content, model="", role="", temp=0):
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

  def test(self):
    test_data = self.create_data("Say this is a test!")
    print(test_data)
    input()

    response = self.post(endpoint='/v1/chat/completions', 
                    data=test_data,
                    headers=self.header)

    if response.status_code != 200:
      raise SentimentAPIError(f"API returned status code {response.status_code}.\n{response.text}")

    return response.json()

# test
if __name__ == '__main__':
  sentimentAPI = SentimentAPI()
  response = sentimentAPI.test()
  print(response)