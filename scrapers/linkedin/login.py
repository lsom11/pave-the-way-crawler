import requests
from bs4 import BeautifulSoup

client = requests.Session()

HOMEPAGE_URL = 'https://www.linkedin.com'
LOGIN_URL = 'https://www.linkedin.com/uas/login-submit'

def login_linkedin():
    html = client.get(HOMEPAGE_URL).content
    soup = BeautifulSoup(html, "html.parser")
    csrf = soup.find(id="loginCsrfParam-login")['value']

    login_credentials = {
        'session_key':'Login',
        'session_password':'Password',
        'loginCsrfParam': csrf,
    }

    client.post(LOGIN_URL, data=login_credentials)

    client.get(HOMEPAGE_URL)
