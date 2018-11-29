from flask import Flask, request, url_for, render_template,Markup
import os
import json
app = Flask(__name__)
with open('publishers.json') as publisher_data:
    allbooks = json.load(publisher_data)
@app.route("/")
def render_main():
    return render_template('about.html')

@app.route("/rank")
def render_page1():
    if 'rank' in request.args:
        rank=(request.args['rank'])
        return render_template('rank.html', options=get_rank_options(allbooks), fact=fact(rank))
    return render_template('rank.html', options=get_rank_options(allbooks) )
   
def get_rank_options(allbooks):
    myList=[]
    for book in allbooks:
        if not book[ "statistics"]["sales rank"] in myList:
            myList.append(book[ "statistics"]["sales rank"] )
    options=""
    for ranks in myList:
        options += Markup("<option value=\"" + str(ranks) + "\">" + str(ranks) + "</option>")
    return options

def fact(rank):
    for  book in allbooks:
        if book[ "statistics"]["sales rank"] == int(rank):
            print( book[ "statistics"]["sales rank"])
            return Markup(str(book [ "statistics"]["sale price"]) +  "sale price" + "<br>" + str( book [ "statistics"]["total reviews"]) + "total reviews" +"<br>" + str( book [ "statistics"]["average rating"]) + "average rating"+"<br>" + str( book[ "daily"]["publisher revenue"]+ "publisher revenue"+ "<br>" + str( book[ "daily"]["amazon revenue"]+ "amazon revenue"+ "<br>" + str( book[ "daily"]["author revenue"]+ "author revenue"+ "<br>" + str( book[ "daily"]["units sold"]+ "units sold" + "<br>" + str( book[ "daily"]["gross sales"]+ "gross sales")
if __name__=="__main__":
    app.run(debug=False, port=54321)
