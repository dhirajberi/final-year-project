import requests
from bs4 import BeautifulSoup
url = "https://cc38a5c76891.ngrok.io/"

r = requests.get(url)
htmlContent = r.content
soup = BeautifulSoup(htmlContent, 'html.parser')
vibration = int(soup.get_text())