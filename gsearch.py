from googleapiclient.discovery import build
from config import API_KEY, CSE_ID

def gsearch(query, startdex):
    service = build("customsearch", "v1", developerKey=API_KEY)
    results = service.cse().list(q=query, cx=CSE_ID, start=startdex).execute()
    return results
