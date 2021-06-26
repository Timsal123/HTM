from flask import Flask,request,jsonify, render_template
import requests
import pickle
import numpy as np
import pandas as pd
app = Flask(__name__)

url = "https://twitter-search2.p.rapidapi.com/twitter/search/tweets"

querystring = {"keyword":"cryptocurrency"}

headers = {
    'x-rapidapi-key': "d02ed07aa2mshca20fb96cc407b2p1abc11jsn90e87ef1178c",
    'x-rapidapi-host': "twitter-search2.p.rapidapi.com"
    }


@app.route('/')
def First():
    return render_template('index.html')
###@app.route('/')
#def demo1():
  # Random recipes
      #querystring = {"keyword":"cryptocurrency"}
      #response = requests.request("GET", url , headers=headers, params=querystring)
      #for i in response:
          #a=[]
          #a.append(i['name'])
          #a.append(i['tweet'])
          #return render_template('index.html', name=a,tweet=a)


@app.route('/penny')
def penny():
    return render_template('penny.html')


@app.route('/meme')
def meme():
    return render_template('meme.html')




@app.route('/dead')
def dead():
    return render_template('dead.html')

@app.route('/bitcoin', methods = ['POST'])
def predictB():
    if request.method== 'POST':
        
        Open = request.form['Open']
        High = request.form['High']
        Low = request.form['Low']
        Close = request.form['Close']
        Volume = request.form['Volume']
        data =[Open,High,Low,Close,Volume]
        data = np.array(data).reshape(-1,5)
        Ps= pickle.load(open('Pickles/bitcoin.pkl','rb'))
        predictionB = Ps.predict(data)[0]
    return render_template('index.html',predictionB= predictionB)

@app.route('/ethereum', methods = ['POST'])
def predictE():
    if request.method== 'POST':
        
        Open = request.form['Open']
        High = request.form['High']
        Low = request.form['Low']
        Close = request.form['Close']
        Volume = request.form['Volume']
        data =[Open,High,Low,Close,Volume]
        data = np.array(data).reshape(-1,5)
        Ps= pickle.load(open('Pickles/ethereumf.pkl','rb'))
        predictionE = Ps.predict(data)[0]
    return render_template('index.html',predictionE= predictionE)

@app.route('/lite', methods = ['POST'])
def predictL():
    if request.method== 'POST':
        
        Open = request.form['Open']
        High = request.form['High']
        Low = request.form['Low']
        Close = request.form['Close']
        Volume = request.form['Volume']
        data =[Open,High,Low,Close,Volume]
        data = np.array(data).reshape(-1,5)
        Ps= pickle.load(open('Pickles/litecoinf.pkl','rb'))
        predictionL = Ps.predict(data)[0]
    return render_template('index.html',predictionL= predictionL)

@app.route('/aeron', methods = ['POST'])
def predictA():
    if request.method== 'POST':
        
        Open = request.form['Open']
        High = request.form['High']
        Low = request.form['Low']
        Close = request.form['Close']
        Volume = request.form['Volume']
        data =[Open,High,Low,Close,Volume]
        data = np.array(data).reshape(-1,5)
        Ps= pickle.load(open('Pickles/aeronf.pkl','rb'))
        predictionA = Ps.predict(data)[0]
    return render_template('index.html',predictionA= predictionA)





@app.route('/dogecoin', methods = ['POST'])
def predictD():
    if request.method== 'POST':
        
        Open = request.form['Open']
        High = request.form['High']
        Low = request.form['Low']
        Close = request.form['Close']
        Volume = request.form['Volume']
        data =[Open,High,Low,Close,Volume]
        data = np.array(data).reshape(-1,5)
        Ps= pickle.load(open('Pickles/dogecoinf.pkl','rb'))
        predictionD = Ps.predict(data)[0]
    return render_template('meme.html',predictionD= predictionD)  



@app.route('/Stellar_lumens', methods = ['POST'])
def predictS():
    if request.method== 'POST':
        
        Open = request.form['Open']
        High = request.form['High']
        Low = request.form['Low']
        Close = request.form['Close']
        Volume = request.form['Volume']
        data =[Open,High,Low,Close,Volume]
        data = np.array(data).reshape(-1,5)
        Ps= pickle.load(open('Pickles/Stellar_lumens.pkl','rb'))
        predictionS = Ps.predict(data)[0]
    return render_template('penny.html',predictionS= predictionS)

@app.route('/Ravencoin', methods = ['POST'])
def predictR():
    if request.method== 'POST':
        
        Open = request.form['Open']
        High = request.form['High']
        Low = request.form['Low']
        Close = request.form['Close']
        Volume = request.form['Volume']
        data =[Open,High,Low,Close,Volume]
        data = np.array(data).reshape(-1,5)
        Ps= pickle.load(open('Pickles/Ravencoin.pkl','rb'))
        predictionR = Ps.predict(data)[0]
    return render_template('penny.html',predictionR= predictionR)  


@app.route('/holocoin', methods = ['POST'])
def predictH():
    if request.method== 'POST':
        
        Open = request.form['Open']
        High = request.form['High']
        Low = request.form['Low']
        Close = request.form['Close']
        Volume = request.form['Volume']
        data =[Open,High,Low,Close,Volume]
        data = np.array(data).reshape(-1,5)
        Ps= pickle.load(open('Pickles/holochainf.pkl','rb'))
        predictionH = Ps.predict(data)[0]
    return render_template('penny.html',predictionH= predictionH)  

@app.route('/Monacoin', methods = ['POST'])
def predictM():
    if request.method== 'POST':
        
        Open = request.form['Open']
        High = request.form['High']
        Low = request.form['Low']
        Close = request.form['Close']
        Volume = request.form['Volume']
        data =[Open,High,Low,Close,Volume]
        data = np.array(data).reshape(-1,5)
        Ps= pickle.load(open('Pickles/Monacoin.pkl','rb'))
        predictionM = Ps.predict(data)[0]
    return render_template('meme.html',predictionM= predictionM)  


if __name__ == '__main__':
    app.run(debug=True)
