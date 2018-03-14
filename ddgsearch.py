from requests import post
from lxml.html import fromstring
"""Didn't work like I wanted it to, but learned a bit from it https://github.com/thibauts/duckduckgo"""

def ddgsearch(query):
	'''
	Returns list of links
	Results not controllable
	'''
	# Sends a POST request to ddg's default search website
	response = post('https://duckduckgo.com/html/', {
		'q': query,
		's': '0'
	})
	# Parses html
	html = fromstring(response.text)
	# Gets elements with the links, giant block is just the path to the links
	alinks = html.xpath("//body[@class='body--html']/div/div/div[@class='serp__results']/\
	div[@class='results']/div[@class='result results_links results_links_deep web-result ']/\
	div[@class='links_main links_deep result__body']/div[@class='result__extras']/\
	div[@class='result__extras__url']/a")
	
	# i.values() returns ['result__url', $url], so i.values()[1] returns the link
	return [i.values()[1] for i in alinks]
