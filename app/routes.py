# A very simple Flask Hello World app for you to get started with...

from flask import render_template, flash, redirect 
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def home():
  return render_template('index.html', title="Home", content='Hello from Flask!')

@app.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    flash('Login requested for user {}, remember_me={}'.format(
      form.username.data, form.remember_me.data))
    return redirect('/index')
  return render_template('login.html', title='Sign In', form=form)

#if __name__ == "__main__":
#  app.run(debug=True)
