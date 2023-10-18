from flask import Flask, render_template

app = Flask(__name__)
#dummy data for rendering posts
posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

@app.route("/")
#for static files 
def hello_world():
    return render_template('home.html',posts=posts, title="yasmin")

@app.route("/about")
def about():
    #instead of returning html we can return a template
    return render_template('about.html')

if __name__=="__main__":
    app.run(host='0.0.0.0',port=50000, debug=True)