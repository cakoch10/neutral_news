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
	urlEndings = ['.com', '.edu', '.org', '.net', '.gov']
	end = 3
	for ending in urlEndings:
		if (end != 3):
			break
		end = url.find(".com") + 4
	s = url[start:end]

	with open('credible.json') as data_file1:
		credibleData = json.load(data_file1)

	with open('notCredible.json') as data_file2:
		notCredibleData = json.load(data_file2)

	credibleDataString = str(credibleData)
	notCredibleDataString = str(notCredibleData)

	#returns the info in string format
	#if s in credibleDataString:
	#	start = credibleDataString.find(s)-1
	#	end = credibleDataString.find("}",start)
	#	return credibleDataString[start:end]
	#else:
	#	start = notCredibleDataString.find(s)-1
	#	end = notCredibleDataString.find("}",start)
	#	return notCredibleDataString[start:end]

	#returns the info in a list
	if s in credibleDataString:
		return [s, credibleData[s]["language"], credibleData[s]["type"], credibleData[s]["notes"]]
	else:
		return [s, notCredibleData[s]["type"], notCredibleData[s]["2nd type"], notCredibleData[s]["3rd type"], notCredibleData[s]["Source Notes (things to know?)"]]


def getTitleFromURL(url):
	
	news_article = Article(url= url, language='en')
	news_article.download()
	news_article.parse()
	return news_article.title.encode("utf-8")

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

	arrayOfURLs = []
	titleOfArticle = getTitleFromURL(url)
	keyWordsOfArticle = getKeyWordsFromURL(url)
	keyWordsGoogleable = ""
	for word in keyWordsOfArticle:
		keyWordsGoogleable += (" " + word)
	keyWordsGoogleable += " news"
	#print ("title of original article: " + titleOfArticle)
	num_page = 3
	search_results = google.search(keyWordsGoogleable, num_page)
	for result in search_results:
		#print(result.name)
		#print(result.link)
		arrayOfURLs.insert(0,str(result.link))
	return arrayOfURLs

def get_html(url):
    header = "Mozilla/5.001 (windows; U; NT4.0; en-US; rv:1.0) Gecko/25250101"
    try:
        request = urllib.request.Request(url)
        request.add_header("User-Agent", header)
        html = urllib.request.urlopen(request).read()
        return html
    except urllib.error.HTTPError as e:
        print("Error accessing:", url)
        if e.code == 503 and 'CaptchaRedirect' in e.read():
            print("Google is requiring a Captcha. " \
                  "For more information see: 'https://support.google.com/websearch/answer/86640'")
        return None
    except Exception as e:
        print("Error accessing:", url)
        print(e)
        return None

def parseList(newsList):
	"""Puts the text of each article in the list into a txt file.
	Parameter newsList: a list of article urls, first being the article the user gave
	and the rest being relevant articles"""
	paper = Article(url=newsList[0], language="en")
	paper.download()
	paper.parse()
	text = paper.text
	paperInfo = findInfo(newsList[0])
	with open(paperInfo[0][:-4], "w") as f:
		f.write(text.encode("utf-8"))
	for url in newsList[1:]:
		paper = Article(url=url, language="en")
		paper.download()
		paper.parse()
		paper.nlp()
		text = paper.text
		with open(paperInfo[0][:-4], "a") as f:
			f.write(text.encode("utf-8"))

def pickArticlesWithOutLabels(url):

	returnArray = []

	arrayOfURLs = google_scrape(url)

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
				returnArray.insert(0, str(url))

	return returnArray

def pickArticlesWithLabels(url):

	numRights = 0
	numMods = 0
	numLefts = 0

	returnArray = []

	arrayOfURLs = google_scrape(url)

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
				returnArray.insert(0, (str(credibleData[x]["type"] + ": " + url)))

	return returnArray

def returnLeaningOfArticle(url):

	with open('credible.json') as data_file1:
		credibleData = json.load(data_file1)

	with open('notCredible.json') as data_file2:
		notCredibleData = json.load(data_file2)

	credibleDataString = str(credibleData)
	notCredibleDataString = str(notCredibleData)

	for x in arrayOfCredibles:
		if x in url:
			return str(credibleData[x]["type"])





