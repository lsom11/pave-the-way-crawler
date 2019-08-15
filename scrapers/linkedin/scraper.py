import requests
from bs4 import BeautifulSoup
from time import sleep
from login import login_linkedin


HOMEPAGE_URL = 'https://www.linkedin.com/in/vanessa-ara%C3%BAjo-371988159/'


def get_url(client, url):
    return client.get(url)


def beautify(client, url):
    source = get_url(client, url)
    return BeautifulSoup(source.content, "html.parser")

def sleep_crawler():
    sleep(3)

def scrape():
    client = login_linkedin()
    page = beautify(client, HOMEPAGE_URL)

    print(page)

    sleep_crawler()

# scrape()

login_linkedin()