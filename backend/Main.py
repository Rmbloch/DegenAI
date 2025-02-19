from CryptoAPI import CryptoAPI

cryptoAPI = CryptoAPI()
response = cryptoAPI.get_coin_list()
print(cryptoAPI.parse_response(response))