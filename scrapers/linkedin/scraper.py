import requests
from bs4 import BeautifulSoup
from time import sleep
# import sys

# sys.path.insert(0, './login.py')
from login import login_linkedin


HOMEPAGE_URL = 'https://www.linkedin.com/in/williamhgates/'


def get_url(client, url):
    return client.get(url)


def beautify(client, url):
    source = get_url(client, url)
    return BeautifulSoup(source.content, "html.parser")

def sleep_crawler():
    sleep(3)

def scrape():
    client = beautify(login_linkedin())
    page = beautify(HOMEPAGE_URL)

    print(page)

    sleep_crawler()

scrape()
