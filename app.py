from flask import Flask
app = Flask(__name__)


@app.route('/')
def index_view():
  return render_template('index.html')


@app.route('/checkURL',methods=['POST'])
def checkURL():
    _url = request.form['inputURL']
    # pass url to method and get json of 5 urls: far left, left, moderate, right, and far right
    # something like return json.dumps({'html':'<span>All fields good !!</span>'})



if __name__ == '__main__':
    app.run()
