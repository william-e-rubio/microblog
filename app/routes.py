from app import app
from app.forms import LoginForm
from flask import render_template, flash, redirect, url_for

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
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
