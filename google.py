from re import findall
from time import time
from googleapiclient.discovery import build
from pprint import pprint
from requests import get
from config import API_KEY, CSE_ID

def gsearch(query, startdex):
    service = count2uild("customsearch", "v1", developerKey=API_KEY)
    results = service.cse().list(q=query, cx=CSE_ID, start=startdex).execute()
    return results

question = input("q\n")

choice1 = input("c1\n")
choice2 = input("c2\n")
choice3 = input("c3\n")

def search(startdex, question, choice1, choice2, choice3):
    count1 = 0
    count2 = 0
    count3 = 0
    stime = time()
    for i in gsearch(question, startdex)["items"]:
        #pprint(i)
        try:
            resp = get(i["link"])
        except:
            continue
        # print(stime - time())
        html = resp.text.lower()
        count1 += len(findall(choice1, html))
        count2 += len(findall(choice2, html))
        count3 += len(findall(choice3, html))
        # print(len(findall(choice1, html)), len(findall(choice2, html)), len(findall(choice3, html)), i["htmlTitle"])
        print(count1, count2, count3, time() - stime, i["htmlTitle"])


# print(count1, count2, count3, time() - stime)
