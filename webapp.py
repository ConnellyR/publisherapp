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
    get_genre_options()
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
            return Markup("<h1>Statistics</h1>" + "<br>" + "<p>" + str(book [ "statistics"]["sale price"]) + "</p>" + "<p>" + "sale price" + "</p>" + "<br>" + "<p>" + str( book [ "statistics"]["total reviews"]) + "</p>" + "<p>" + "total reviews" +"</p>"+"<br>" + "<p>" + str( book [ "statistics"]["average rating"]) + "</p>" + "<p>" + "average rating" +"</p>"+"<br>" + "<h1>Revenue</h1>" +"<br>" + "<p>" + str( book[ "daily"]["publisher revenue"]) +"</p>"+ "<p>" +"publisher revenue"+ "</p>"+"<br>" + "<p>" + str( book[ "daily"]["amazon revenue"]) + "</p>" + "<p>" +"amazon revenue"+ "</p>" +"<br>" + "<p>" + str( book[ "daily"]["author revenue"]) + "</p>"+ "<p>" +"author revenue"+ "</p>" +"<br>" + "<p>" + str( book[ "daily"]["units sold"]) +"</p>"+ "<p>" +" units sold" +"</p>"+ "<br>" + "<p>" +  str( book[ "daily"]["gross sales"]) + "</p>"+ "<p>" + "gross sales"+ "</p>")
          
@app.route("/Graph")
def render_page2():
    return render_template('Graph.html', data=get_genre_options())
    
def get_genre_options():  
    dict= { }
    total = 0
    for books in allbooks:
        if books["genre"] in dict:
            dict [books["genre"]]= dict [books["genre"]]+1
        else:
            dict [books["genre"]]= 1
        total = total +1
    print(dict )
    print(total)
    for  genre in dict:
        dict[genre]=dict[genre]/total
    print(dict)
    
    s=""
    for genre in dict: 
        s=s +'{y:' + str(dict[genre]*100) +', label:' + '"' + genre + '"' + '},'
        print(s)
    print(s)
    return s
    
    
    @app.route("/average")
def render_page3():
    if 'average' in request.args:
        rank=(request.args['average'])
        return render_template('average.html', info=info(average))
    return render_template('average.html')
   
    
def info(average):
    for  book in allbooks:
        if book[ "statistics"]["sales rank"] == in range:
            print( book[ "statistics"]["sales rank"])  
    
    
    
if __name__=="__main__":
    app.run(debug=True, port=54321)

    
    
  
    
    