from flask import render_template, flash, redirect, url_for, session
from app import app
from app.forms import LoginForm
from app.models import Engineers

@app.route('/')
@app.route('/index')
def index():
  if not session.get('logged_in'):
    return redirect(url_for('login'))
  return render_template('index.html', title="Home", content='Hello from Flask!')

@app.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    user = Engineers.query.filter_by(username=form.username.data).first()
    print(user)
    
    if user is None or not user.check_password(form.password.data):
      flash('Invalid username or password')
      return redirect(url_for('login'))

    flash(f'Login requested for user={form.username.data}, \
      remember_me={form.remember_me.data}')
    session['logged_in'] = True
    session['username'] = user.username
    return redirect(url_for('index'))
  return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
  session.pop('logged_in', None)
  return redirect(url_for('login'))

#if __name__ == "__main__":
#  app.run(debug=True)
