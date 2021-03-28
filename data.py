import requests
url = "https://8b63b29227d9.ngrok.io/"
res = requests.get(url)
vibration = int(res.text)