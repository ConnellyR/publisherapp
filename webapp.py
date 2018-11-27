from flask import Flask, url_for, render_template
import os
import json
app = Flask(__name__)

@app.route("/")
def render_main():
     with open('publisher.json') as publisher_data:
        books = json.load(publisher_data)
    return render_template('about.html')

@app.route("/rank")
def render_page1():
    return render_template('rank.html')
   
def get_rank_options(counties):
    myList=[]
    for county in counties:
        if not county["State"] in myList:
            myList.append(county["State"] )
    options=""
    for State in myList:
        options += Markup("<option value=\"" + State + "\">" + State + "</option>")
    return options
if __name__=="__main__":
    app.run(debug=False, port=54321)
