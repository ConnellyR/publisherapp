from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template('about.html')

@app.route("/first")
def render_page1():
    return render_template('rank.html')
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
