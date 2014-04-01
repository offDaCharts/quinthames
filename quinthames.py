import json
import requests

from flask import Flask, render_template, redirect, url_for, request, Response, abort, make_response, flash
from pymongo import Connection
from functools import wraps

app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = 'this key is so secret'
      
      
@app.route('/')
def show_home():
    return render_template('home.html')

@app.route('/resume')
def show_resume():
    return render_template('resume.html')

@app.route('/projects')
@app.route('/projects/chatter')
def show_chatter():
    return render_template('chatter.html')

@app.route('/projects/nuclear_fusor')
def show_nuclear_fusor():
    return render_template('nuclear_fusor.html')

@app.route('/projects/bike_with_friends')
def show_bike_with_friends():
    return render_template('bike_with_friends.html')

@app.route('/projects/autonomous_SAR')
def show_autonomous_SAR():
    return render_template('autonomous_SAR.html')

@app.route('/projects/autonomous_SAR/report')
def show_autonomous_SAR_report():
    return render_template('SAR_report.html')

@app.route('/projects/crow_deterrent')
def show_crow_deterrent():
    return render_template('crow_deterrent.html')

@app.route('/projects/crow_deterrent/report')
def show_crow_deterrent_report():
    return render_template('crow_report.html')

@app.route('/projects/very_such_much')
def show_very_such_much():
    return render_template('very_such_much.html')

@app.route('/contact')
def show_contact():
    return render_template('contact.html')

@app.route('/402')
def show_contact():
    return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ", code=302)


# App Configuration
# This section holds all application specific configuration options.

if __name__ == '__main__':
	app.debug=True
	app.run(host='0.0.0.0', port=5656, processes=1)
