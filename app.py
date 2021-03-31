# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 16:16:20 2021
"""

from flask import Flask, render_template, request
#from googleapiclient.discovery import build
from apiclient.discovery import build

api_key ="----use your api key here---"
yotube = build('youtube','v3',developerKey=api_key)

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/search', methods=['POST'])
def predict():
    if request.method == 'POST':
        search = (request.form['Search'])
        
        req = yotube.search().list(q=search,part='snippet',type='video')
        res = req.execute()
        
        listt=[]
        for item in res['items']:
            id=item['id']['videoId']
            youtube="https://youtube.com/embed/"
            id=youtube+id
            listt.append(id)        
        
        
        return render_template('index.html')
    
if __name__ == '__main__':
	app.run(debug=True)    

    
