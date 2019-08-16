import requests
from bs4 import BeautifulSoup
from time import sleep

SEARCH_URL = 'https://www.google.com/search?q='

def beautify(input_search):
    source = requests.get(SEARCH_URL + input_search)
    return BeautifulSoup(source.content, 'html.parser')

def sleep_crawler():
    sleep(3)

def scrape(input_search):
    page = beautify(input_search)

    print(page)

    headline_results = page.find_all('div', class_ ='srg')
    for h in headline_results:
        print(h)

    sleep_crawler()

name = input('Enter your name:')
scrape(name.replace(" ", "+"))
