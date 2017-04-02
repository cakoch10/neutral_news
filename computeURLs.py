#import urllib.request
from __future__ import unicode_literals
import newspaper
#import word2vec
#import rpy2.robjects as ro

#from newspaper import Article
#import urllib2
import json
import nltk
import os
#from nltk.corpus.reader.plaintext import PlaintextCorpusReader
import csv
from sklearn.feature_extraction.text import TfidfVectorizer

def compareSimilarity(urlone, urltwo):
    first_article = Article(url=urlone, language='en')
    first_article.download()
    first_article.parse()
    second_article = Article(url=urltwo, language='en')
    second_article.download()
    second_article.parse()
    doc[0] = first_article.text
    doc[1] = second_article.text
    documents = doc
    tfidf = TfidfVectorizer().fit_transform(documents)
    pairwise_similarity = tfidf * tfidf.T
    return pairwise_similarity

def buildModel():
    corpusdir = 'farRight/' # Directory of corpus.
    directories = ['farRight/', 'farLeft/', 'moderate/', 'centerRight/', 'centerLeft']
    input_file = open('alldata.txt', 'w')
    id_ = 0
    for directory in directories:
        rootdir = os.path.join('', directory)
        for subdir, dirs, files in os.walk(rootdir):
            for file_ in files:
                with open(os.path.join(subdir, file_), 'r') as f:
                    doc_id = '_*%i' % id_
                    text = f.read()
                    #text = str.decode(text,'utf-8')
                    tokens = nltk.word_tokenize(text)
                    doc = ' '.join(tokens).lower()
                    doc = doc.encode('ascii', 'ignore')
                    input_file.write('%s %s\n' % (doc_id, doc))
        id_ = id_ + 1
    input_file.close()
    #word2vec.doc2vec('alldata.txt', cbow=0, size=100, window=10, negative=5, hs=0, sample='1e-4', threads=12, iter_=20, min_count=1, verbose=True)
    word2vec.doc2vec('alldata.txt', 'vectors.bin', cbow=0, size=100, window=10, negative=5, hs=0, sample='1e-4', threads=12, iter_=20, min_count=1, verbose=True)

    f = open('final_table.csv', 'rb')
    # reader = csv.reader(f)
    # headers = reader.next()
    # column = {}
    # for h in headers:
    #     column[h] = []
    # for row in reader:
    #     for h, v in zip(headers, row):
    #         column[h].append(v)
    # #column contains a dictionary of the data we need to load to model
    # arr[0] = column[""]
    # X =

    ##########EXECUTE CODE FROM WITHIN PYTHON!!!


    #newcorpus = PlaintextCorpusReader(corpusdir, '.*')
    #documents = [(list(newcorpus.words(fileid)), category) for category in newcorpus.categories() for fileid in newcorpus.fileids(category)]




def scrapeFarRight():
    farRight = newspaper.build('http://www.breitbart.com/big-government/',memoize_articles=False)
    i = 0
    for article in farRight.articles:
        article.download()
        article.parse()
        with open("farRight/article" + str(i) + ".txt", 'w') as out:
            out.write(article.text + '\n')
        i = i+1

def scrapeCenterRight():
    centerR = newspaper.build('http://foxnews.com/us.html',memoize_articles=False)
    i = 0
    for article in centerR.articles:
        article.download()
        try:
            article.parse()
        except:
            pass
        with open("centerRight/article" + str(i) + ".txt", 'w') as out:
            out.write(article.text + '\n')
        i = i+1
    print(i)

def scrapeModerate():
    moderate = newspaper.build('http://cbsnews.com/us/',memoize_articles=False)
    i = 0
    for article in moderate.articles:
        article.download()
        try:
            article.parse()
        except:
            pass
        with open("moderate/article" + str(i) + ".txt", 'w') as out:
            out.write(article.text + '\n')
        i = i+1
    print(i)

def scrapeCenterLeft():
    centerL = newspaper.build('http://bbc.com/news/world/us_and_canada',memoize_articles=False)
    i = 0
    for article in centerL.articles:
        article.download()
        try:
            article.parse()
        except:
            pass
        with open("centerLeft/article" + str(i) + ".txt", 'w') as out:
            out.write(article.text + '\n')
        i = i+1
    print(i)

def scrapeFarLeft():
    farLeft = newspaper.build('http://dailykos.com/blogs/main',memoize_articles=False)
    i = 0
    for article in farLeft.articles:
        article.download()
        try:
            article.parse()
        except:
            pass

        with open("farLeft/article" + str(i) + ".txt", 'w') as out:
            out.write(article.text + '\n')
        i = i+1
    print(i)

def waste():


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
    print("test")


def compute(url):
    return json.dumps({'url1': url1, 'url2': url2, 'url3': url3, 'url4': url4, 'url5': url5})
