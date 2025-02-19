# implementation of AbstractAPI 

from requests import get, post, put, delete

class AbstractAPI:
  base_url = None
  api_key = None

  def __init__(self, base_url, api_key):
    self.base_url = base_url
    self.api_key = api_key

  def get(self, endpoint="", params=None, headers=None):
    return get(self.base_url + endpoint, params=params, headers=headers)

  def post(self, endpoint="", data=None, headers=None):
    return post(self.base_url + endpoint, json=data, headers=headers)
  
  def put(self, endpoint="", data=None, headers=None):
    return put(self.base_url + endpoint, json=data, headers=headers)
  
  def delete(self, endpoint="", headers=None):
    return delete(self.base_url + endpoint, headers=headers)

  def parse_response(self, response):
    return response.json()
