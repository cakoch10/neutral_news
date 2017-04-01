#import urllib.request
from newspaper import Article
import urllib2, json

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


    farRight = newspaper.build('http://www.breitbart.com/big-government/')
    print farRight.articles

    #farRight = Article(url="http://www.breitbart.com/big-government/", language='en')
    farRight.download()





def compute(url):



    return json.dumps({'url1': url1, 'url2': url2, 'url3': url3, 'url4': url4, 'url5': url5})
