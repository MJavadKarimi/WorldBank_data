import requests
from bs4 import BeautifulSoup

# this is a crawler for extracting prodocts price

url = 'https://samaneahan.com/price/beam-common'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

prices_list = []

for price in soup.find_all('span', class_='cell-price'):
    price = soup.find('span', class_='cell-price').text
    if price:
        prices_list.append(price)

print(prices_list)