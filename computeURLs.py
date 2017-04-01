#import urllib.request
import newspaper
#from newspaper import Article
#import urllib2
import json


def test1():
    s = 0
    for i in range(1, 10):
        s = s+1
        print(s)

def scrapeFarRight():
    farRight = newspaper.build('http://www.breitbart.com/big-government/',memoize_articles=False)
    i = 0
    for article in farRight.articles:
        article.download()
        article.parse()
        with open("farRight/article" + str(i) + ".txt", 'a') as out:
            out.write(article.text + '\n')
        i = i+1

def scrapeCenterRight():
    centerR = newspaper.build('http://foxnews.com/us.html',memoize_articles=False)
    i = 0
    for article in centerR.articles:
        article.download()
        article.parse()
        with open("centerRight/article" + i + ".txt", 'a') as out:
            out.write(article.text + '\n')
        i = i+1

def scrapeModerate():
    moderate = newspaper.build('http://cbsnews.com/us/',memoize_articles=False)
    i = 0
    for article in moderate.articles:
        article.download()
        article.parse()
        with open("moderate/article" + i + ".txt", 'a') as out:
            out.write(article.text + '\n')
        i = i+1

def scrapeCenterLeft():
    centerL = newspaper.build('http://bbc.com/news/world/us_and_canada')
    i = 0
    for article in centerL.articles:
        article.download()
        article.parse()
        with open("centerLeft/article" + i + ".txt", 'a') as out:
            out.write(article.text + '\n')
        i = i+1


def scrapeFarLeft():
    farLeft = newspaper.build('http://dailykos.com/blogs/main')
    i = 0
    for article in farLeft.articles:
        article.download()
        article.parse()
        with open("centerLeft/article" + i + ".txt", 'a') as out:
            out.write(article.text + '\n')
        i = i+1

def scrapeNews():
    # urllib2.urlopen("http://example.com/foo/bar").read()
    # https://newsapi.org/v1/articles?source=breitbart-news&sortBy=&apiKey=989c61d67d234d3fa19d1ec4e6c5b361
    #u = urllib.request.urlopen("https://newsapi.org/v1/articles?source=breitbart-news&sortBy=&apiKey=989c61d67d234d3fa19d1ec4e6c5b361").read()

    #fR = urllib2.urlopen("https://newsapi.org/v1/articles?source=breitbart-news&sortBy=top&apiKey=989c61d67d234d3fa19d1ec4e6c5b361").read()
    #fR2 = json.loads(fR)
    # print json.dumps(fR2, indent = 4, sort_keys = True)
    #print len(fR2['articles'])

    #L = urllib2.urlopen("https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=989c61d67d234d3fa19d1ec4e6c5b361").read()
    #L2 = json.loads(L)
    # print json.dumps(L2, indent = 4, sort_keys = True)
    #print len(L2['articles'])
    # http://www.breitbart.com/big-government/ cbs_paper = newspaper.build('http://cbs.com')
    # strFR = ""
    #farRight = newspaper.build('http://breitbart.com/big-government')
    #print(strFR)
    #print(len(farRight.articles))
    #farRight = Article(url="http://www.breitbart.com/big-government/", language='en')
    #farRight.download()
    #centerRight = newspaper.build('http://foxnews.com/us.html')
    #center = newspaper.build('http://cbsnews.com/us/')
    #centerLeft = newspaper.build('http://bbc.com/news/world/us_and_canada')
    #farLeft = newspaper.build('http://newyorker.com/news')
    #farLeft = newspaper.build('http://dailykos.com/blogs/main') # Possible candidate?



def compute(url):



    return json.dumps({'url1': url1, 'url2': url2, 'url3': url3, 'url4': url4, 'url5': url5})
