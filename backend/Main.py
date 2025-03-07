from CryptoAPI import CryptoAPI

cryptoAPI = CryptoAPI()
response = cryptoAPI.get_coin_list()
for i, coin in enumerate(response):
  print(f"{i:02d}: {coin}")