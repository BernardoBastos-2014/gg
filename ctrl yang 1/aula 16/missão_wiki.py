import requests.get(url)
from bs4 import BeautifulSoup

soup = BeautifulSoup(resposta.content, 'html.parser')

titulo = soup.find('h1')
print(titulo.text.strip())


primera_citação = soup.find('span', class_ = "text")
print(primera_citação)