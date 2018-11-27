from flask import Flask, url_for, render_template
import os
import json
app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template('about.html')

@app.route("/rank")
def render_page1():
    with open('publishers.json') as publisher_data:
        allbooks = json.load(publisher_data)
    return render_template('rank.html', options=get_rank_options(allbooks))
   
def get_rank_options(allbooks):
    myList=[]
    for book in allbooks:
        if not book[ "statistics"]["sales rank"] in myList:
            myList.append(book[ "statistics"]["sales rank"] )
    options=""
    for ranks in myList:
        options += Markup("<option value=\"" + ranks + "\">" + ranks + "</option>")
    return options
if __name__=="__main__":
    app.run(debug=False, port=54321)
