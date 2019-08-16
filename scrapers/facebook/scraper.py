# import requests
# from bs4 import BeautifulSoup


# SEARCH_URL = "https://facebook.com/search/top/?q="
# SPACE_CHARACTER = '%20'
# name= input("Enter your name:")
# name = name.replace(" ", SPACE_CHARACTER)

# page = requests.get(SEARCH_URL + name)

# soup = BeautifulSoup(page.text, 'html.parser')

# # Remove bottom links
# last_links = soup.find(class_='AlphaNav')
# print(last_links)
# # last_links.decompose()

# # artist_name_list = soup.find(class_='BodyText')
# # artist_name_list_items = artist_name_list.find_all('a')

# # for artist_name in artist_name_list_items:
# #     print(artist_name.prettify())