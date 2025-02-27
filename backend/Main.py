from CryptoAPI import CryptoAPI

cryptoAPI = CryptoAPI()
response = cryptoAPI.get_coin_list()
for coin in response:
  print(coin)