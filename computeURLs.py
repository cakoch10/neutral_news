#import urllib.request
import newspaper
#from newspaper import Article
#import urllib2
import json

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

    farRight = newspaper.build('http://www.breitbart.com/big-government/',memoize_articles=False)
    # strFR = ""
    #farRight = newspaper.build('http://breitbart.com/big-government')

    for article in farRight.articles:
        print(article.url)
        #strFR += article.url + '\n'
        with open("farRight.txt", 'a') as out:
            out.write(article.url + '\n')
        #print(article.url)
    print("test")
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
