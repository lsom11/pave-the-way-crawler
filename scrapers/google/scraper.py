from googleapiclient.discovery import build

API_KEY = 'AIzaSyC2uE6WMCPO2xcTsqULI_wa_iwPhP5Zzj0'
CSE_ID = '013040238308795042536:ovfr8s2onym'


def google_search(search_term, api_key, cse_id, **kwargs):
    filter_itens(get_itens(get_result(search_term, api_key, cse_id, **kwargs)))

def get_result(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    return service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()


def get_itens(result):
    return result['items']

def filter_itens(items):
    for item in items:
        if item['displayLink'] == 'br.linkedin.com' or item['displayLink'] == 'pt-br.facebook.com':
            print(item['formattedUrl'])


google_search("Marcel Rapanelli", API_KEY, CSE_ID)

