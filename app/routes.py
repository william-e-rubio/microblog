from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/login')
def login():
	form = LoginForm()
	return render_template('login.html', title='Sign In', form=form)

@app.route('/')
@app.route('/index')

def index():	
	user = {'username': 'William Rubio'}
	posts = [
		{
			'author' : {'username' : 'John'},
			'body' : 'Beautiful day in Belize!'
		},
		{
			'author' : {'username' : 'James'},
			'body' : 'The day in the life of a 24 year old software engineer living in Belize!'
			
		}
	]
	return render_template('index.html', title='Home', user=user, posts=posts)
