import requests
from bs4 import BeautifulSoup
url = "https://8b63b29227d9.ngrok.io/"

r = requests.get(url)
htmlContent = r.content
soup = BeautifulSoup(htmlContent, 'html.parser')
vibration = int(soup.get_text())