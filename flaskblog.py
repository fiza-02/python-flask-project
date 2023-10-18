from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
#for static files 
def hello_world():
    return render_template('home.html')

@app.route("/about")
def about():
    #instead of returning html we can return a template
    return render_template('about.html')

if __name__=="__main__":
    app.run(host='0.0.0.0',port=50000, debug=True)