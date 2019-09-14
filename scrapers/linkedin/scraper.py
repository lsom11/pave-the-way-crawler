import requests
from bs4 import BeautifulSoup
from time import sleep


CLIENT = requests.Session()
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
headers = {'User-Agent': user_agent}

HOMEPAGE_URL = 'https://www.linkedin.com/authwall?trk=bf&trkInfo=bf&originalReferer=&sessionRedirect=https%3A%2F%2Fwww.linkedin.com%2Fcompany%2Fbiotech%2F'
LOGIN_URL = 'https://www.linkedin.com/uas/login-submit'
PROFILE_URL = 'https://www.linkedin.com/in/vanessa-ara%C3%BAjo-371988159/'

class LinkedInScraper():
    def login_linkedin():
        html = CLIENT.get(HOMEPAGE_URL, headers=headers).content
        soup = BeautifulSoup(html, "html.parser")

        login_credentials = {
            'session_key': 'pavethewaycompany@gmail.com',
            'session_password': 'FIAP2019',
        }

        CLIENT.post(LOGIN_URL, data=login_credentials)
        return soup

    def get_url():
        return CLIENT.get(PROFILE_URL)


    def beautify():
        source = get_url()
        return BeautifulSoup(source.content, "html.parser")

    def sleep_crawler():
        sleep(3)

    def scrape():
        url = 'https://www.linkedin.com/company/10073529?trk=tyah&trkInfo=clickedVertical%3Acompany%2CclickedEntityId%3A10073529%2Cidx%3A1-1-1%2CtarId%3A1461132316737%2Ctas%3Adastrong%20'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")
        login_linkedin()
        page = beautify()

        sleep_crawler()
