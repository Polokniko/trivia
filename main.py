from re import findall, compile
from time import time
from gsearch import gsearch
from ddgsearch import ddgsearch
from requests import get


def split(text):
    """Splits 'vv's into different (searches)? Returns regex
    Not sure what it's called
    """
    if 'vv' in text:
        result = ''
        text = text.split('vv')
        for i in text:
            result += f"({i})"
            result += '|' if i != text[-1] else ''
        
        return compile(result)
    return text


def search(qsearchf, question, choice1, choice2, choice3):
    count1 = 0
    count2 = 0
    count3 = 0
    stime = time()
    """Google Custom Search Engine Search"""
    # for i in qsearchf(question, startdex)["items"]:
    #     #pprint(i)
    #     try:
    #         resp = get(i["link"])
    #     except:
    #         continue
    #     # print(stime - time())
    #     html = resp.text.lower()
    #     count1 += len(findall(choice1, html))
    #     count2 += len(findall(choice2, html))
    #     count3 += len(findall(choice3, html))
    #     # print(len(findall(choice1, html)), len(findall(choice2, html)), len(findall(choice3, html)), i["htmlTitle"])
    #     print(count1, count2, count3, time() - stime, i["htmlTitle"])
    """DuckDuckGo Results Search"""
    for i in ddgsearch(question):
        try:
            resp = get(i)
        except Exception as e:
            print(e)
            continue
        
        html = resp.text.lower()
        count1 += len(findall(choice1, html))
        count2 += len(findall(choice2, html))
        count3 += len(findall(choice3, html))

        print(count1, count2, count3, time() - stime, i)

question = input("q\n")

choice1 = split(input("c1\n").lower())
choice2 = split(input("c2\n").lower())
choice3 = split(input("c3\n").lower())

# startdex = 1
while True:
    search(ddgsearch, question, choice1, choice2, choice3)
    # startdex += 10
