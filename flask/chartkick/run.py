#!/usr/bin/env python
# coding=utf-8
from flask import Flask, jsonify, render_template, request  
import chartkick  
import json
  
#app = Flask(__name__, static_folder=chartkick.js())  
app = Flask(__name__)  
app.jinja_env.add_extension("chartkick.ext.charts")  
 
@app.route('/')  
@app.route('/index')  
def index():  
    value = {'谷歌': 52.9, 'Opera': 1.6, 'Firefox': 27.7}  
    return render_template('index.html', data=json.dumps(value, encoding='utf-8',indent=4))  
  
  
if __name__ == "__main__":  
    app.run(host="0.0.0.0",debug=True)  
