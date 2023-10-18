from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

'''
>>> import secrets
>>> secrets.token_hex(16)
'f8d1e7b246c52fd81b103f0e265294ca'
'''
# when we use these forms we need a secret key , a secret key will protect against modifiying cookies and cross-site request forgery attacks
app.config['SECRET_KEY'] = 'fac072214929018288a5d4c197bbf3f0'
# use random set of characters for secret key
# dummy data for rendering posts

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
# for static files
def home():
    return render_template('home.html', posts=posts, title="yasmin")


@app.route("/about")
def about():
    # instead of returning html we can return a template
    return render_template('about.html')


@app.route("/register",methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register', form=form)
    
@app.route("/login",methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html',title='=Login', form=form)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)
