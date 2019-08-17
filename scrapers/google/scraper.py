from googleapiclient.discovery import build

SEARCH_URL = 'https://www.google.com/search?q='
API_KEY = 'AIzaSyC2uE6WMCPO2xcTsqULI_wa_iwPhP5Zzj0'
CSE_ID = '013040238308795042536:ovfr8s2onym'


def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    return service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()


def get_itens(result):
    return result['items']

def get_good_itens(items):
    for item in items:
        if item['displayLink'] == 'br.linkedin.com' or item['displayLink'] == 'pt-br.facebook.com':
            print(item['formattedUrl'])


result = google_search("Marcel Rapanelli", API_KEY, CSE_ID)
items = get_itens(result)
get_good_itens(items)
