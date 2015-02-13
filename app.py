from flask import Flask, url_for, render_template,request,session,flash,redirect,jsonify
import requests
from urllib import urlopen
import json
import oauth2 as oauth
app = Flask(__name__)
app.secret_key = 'development key'
@app.route('/', methods=['POST', 'GET'])
def index():
	return render_template('index.html')
@app.route('/github',methods=['POST', 'GET'])
def github():
	name=request.form['text']
	url = 'https://api.github.com/users/'+name+'/repos'
	req=requests.get(url).json()
	s=''
	for valu in req:
		s=s+'<li>'+valu['name']+'</li>'
	s='<ol>'+s+'</ol>'
	return jsonify({1:s})

if __name__ == '__main__':
	app.run(debug=True)

