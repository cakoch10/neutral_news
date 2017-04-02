from flask import Flask, jsonify, render_template, request, json
from news import *
app = Flask(__name__)

@app.route('/')
def index_view():
  return render_template('index.html')

@app.route('/checkURL', methods=['POST'])
def checkURL():
    _url = request.json['inputURL']
    url_arr = pickArticlesWithOutLabels(_url)
    url_arr = filter(lambda a: a != _url, url_arr)
    url_arr = set(url_arr)
    url_arr = list(url_arr)
    url_titles = dict.fromkeys(url_arr)
    url_leans = dict.fromkeys(url_arr)
    for url in url_titles:
        url_titles[url] = getTitleFromURL(url)
    for url in url_leans:
        url_leans[url] = returnLeaningOfArticle(url)
    # google_scrape(_url)
    # url_arr = pickArticlesWithOutLabels()
    originalLeans = returnLeaningOfArticle(_url)
    print(url_arr)
    print(url_titles)
    print(url_leans)
    return json.dumps({'originalLeans': originalLeans, 'url': _url, 'url_arr': url_arr, 'url_titles': url_titles, 'url_leans': url_leans})
    # pass url to method and get json of 5 urls: far left, left, moderate, right, and far right
    # something like return json.dumps({'html':'<span>All fields good !!</span>'})

if __name__ == '__main__':
    app.run()
