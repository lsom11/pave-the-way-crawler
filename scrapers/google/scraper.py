from googleapiclient.discovery import build

SEARCH_URL = 'https://www.google.com/search?q='
API_KEY = 'AIzaSyC2uE6WMCPO2xcTsqULI_wa_iwPhP5Zzj0'
CSE_ID = '013040238308795042536:ovfr8s2onym'


def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=API_KEY)
    return service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()

result = google_search("Guilherme+Abreu", API_KEY, CSE_ID)
print(result)