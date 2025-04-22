from CryptoAPI import CryptoAPI
import os
from PIL import Image

cryptoAPI = CryptoAPI()
response = cryptoAPI.get_coin_list()
for i, coin in enumerate(response):
  print(f"{i:02d}: {coin}")
  print(coin.image_url)
  # Download the image
  # get image from the url via wget
  os.system(f"wget {coin.image_url} -O {coin.__hash__()}.png")
  # Open the image
  with Image.open(f"{coin.__hash__()}.png") as img:
    img.show()
  # rm image
  os.remove(f"{coin.__hash__()}.png")