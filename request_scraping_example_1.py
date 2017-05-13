import requests
from bs4 import BeautifulSoup
import sys

# enter the url to be scraped
url_to_scrape = 'https://www.snapdeal.com/product/refurbished-motorola-moto-m-64gb/641253021263'

# send a request to the url
response = requests.get(url_to_scrape)

# convert it to a soup object
soup = BeautifulSoup(response.text, 'lxml')

# extract the information you want to
sys.stdout.write(soup.find('h1', attrs={'itemprop': 'name'}).get('title')+'\n')
sys.stdout.write(soup.find('span', attrs={'itemprop': 'price'}).text)
