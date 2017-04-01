# Fake News Thing
# Raymone Radi (rsr242)
# 03/31/17
"""Reads fake news URLs 

Tells you if this good or bad!"""

import json
import urllib
import urllib2
from pprint import pprint
import newspaper
from newspaper import Article
from google import google

arrayOfURLs = []
arrayOfKeyWords = []
arrayOfCredibles = []
arrayOfNotCredibles = []

def findInfo(url):

	"""Returns relevant information regarding the news source and article.

	Takes the url string s. With the string, site title is extracted and
	compared to credible.json and notCredible.json. Once site title is found
	in either of the jsons, the rest of the data is extracted. 

	Parameter url: the url of the subject article
	Precondition: url is a string of a valid website url."""

	start = url.find("www.") + 4
	if (start == 3):
		start = 0
	end = url.find(".com") + 4
	s = url[start:end]

	with open('credible.json') as data_file1:
		credibleData = json.load(data_file1)

	with open('notCredible.json') as data_file2:
		notCredibleData = json.load(data_file2)

	credibleDataString = str(credibleData)
	notCredibleDataString = str(notCredibleData)

	#returns the info in string format
	if s in credibleDataString:
		start = credibleDataString.find(s)-1
		end = credibleDataString.find("}",start)
		return credibleDataString[start:end]
	else:
		start = notCredibleDataString.find(s)-1
		end = notCredibleDataString.find("}",start)
		return notCredibleDataString[start:end]

	#returns the info in a list
	if s in credibleDataString:
		return [s, credibleData[s]["language"], credibleData[s]["type"], credibleData[s]["notes"]]
	else:
		return [s, notCredibleData[s]["type"], notCredibleData[s]["2nd type"], notCredibleData[s]["3rd type"], notCredibleData[s]["Source Notes (things to know?)"]]


def getTitleFromURL(url):
	
	news_article = Article(url= url, language='en')
	news_article.download()
	news_article.parse()
	return news_article.title

def getKeyWordsFromURL(url):
	
	returnArray = []
	news_article = Article(url= url, language='en')
	news_article.download()
	news_article.parse()
	news_article.nlp()
	for word in news_article.keywords:
		word = str(word)
		returnArray.insert(0,word)
	return returnArray

def google_scrape(url):

	titleOfArticle = getTitleFromURL(url)
	keyWordsOfArticle = getKeyWordsFromURL(url)
	#print ("title of original article: " + titleOfArticle)
	num_page = 3
	search_results = google.search(titleOfArticle, num_page)
	for result in search_results:
		#print(result.name)
		#print(result.link)
		arrayOfURLs.insert(0,str(result.link))

def pickArticles():

	with open('credible.json') as data_file1:
		credibleData = json.load(data_file1)

	with open('notCredible.json') as data_file2:
		notCredibleData = json.load(data_file2)

	credibleDataString = str(credibleData)
	notCredibleDataString = str(notCredibleData)

	for key1 in credibleData:
		arrayOfCredibles.insert(0,(str(key1)))

	for url in arrayOfURLs:
		for x in arrayOfCredibles:
			if x in url:
				print url
		#for x in arrayOfNotCredibles:
			#if x in url:
				#print "Not safe!"

	#print arrayOfKeyWords





