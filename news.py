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
	keyWordsGoogleable = ""
	for word in keyWordsOfArticle:
		keyWordsGoogleable += (" " + word)
	keyWordsGoogleable += " news"
	print keyWordsGoogleable
	#print ("title of original article: " + titleOfArticle)
	num_page = 3
	search_results = google.search(keyWordsGoogleable, num_page)
	for result in search_results:
		#print(result.name)
		#print(result.link)
		arrayOfURLs.insert(0,str(result.link))

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

def pickArticlesWithOutLabels():

	returnArray = []

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

def pickArticlesWithLabels():

	returnArray = []

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

def similarity(url1, url2):
	"""Constructs a list of keywords from the two articles found at url1 and url2 and gets the average similarity"""

	paper1 = Article(url=url1, language="en")
	paper2 = Article(url=url2, language="en")
	paper1.download()
	paper2.download()
	paper1.parse()
	paper2.parse()
	paper1.nlp()
	paper2.nlp()
	keywords1 = paper1.keywords
	keywords2 = paper2.keywords
	sameCounter = 0
	if (len(keywords1) == 0 and len(keywords2) == 0):
		return 0
	for word1 in keywords1:
		for word2 in keywords2:
			if word1 == word2:
				sameCounter = sameCounter + 2
	return 1.0*sameCounter/(len(keywords1)+len(keywords2))

def plotData(url, dataset):
	"""Constructs a plot of the similarity index with a given article

	Parameter url: url the subject article
	Precondition: url

	Parameter dataset: list of article urls
	Precondition: list of article urls. """

	mainArticle = Article(url=url, language="en")
	plotData = []
	typeList = ["far left", "center left", "moderate", "center right", "far right"]
	for article in dataset:
		plotData = plotData + [typeList.index(findInfo(article)[2]), similarity(url,article)]
	print plotData
	plt.boxplot(plotData, showbox = False, showcaps = False)
	plt.ylabel('similarity index')
	plt.show()



