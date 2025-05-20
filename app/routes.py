from flask import render_template, flash, redirect, url_for, session, request
from app import app, db
from app.forms import LoginForm, ConditionsFilter
import app.models as models 
from sqlalchemy import select, desc
from config import Config

@app.route('/')
@app.route('/index')
def index():
  if not session.get('logged_in'):
    return redirect(url_for('login'))
  return render_template('index.html', title="Поверки",
    username=f"{session.get('username')}",
    content='Hello from Flask!')

@app.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()

  if form.validate_on_submit():
    #user = models.Engineers.query.filter_by(username=form.username.data).first()
    user = models.Engineers().get_by_name(form.username.data)
    
    if user is None or not user.check_password(form.password.data):
      flash('Invalid username or password')
      return redirect(url_for('login'))

    flash(f'Login requested for user={form.username.data}')
    session['logged_in'] = True
    session['username'] = user.username
    session['user_id'] = user.id
    session['current_page'] = "verifications"
    return redirect(url_for('index'))
  return render_template('login.html', title='Войти', form=form)

@app.route('/logout')
def logout():
  session.pop('logged_in', None)
  session.pop('username', None)
  session.pop('user_id', None)
  session.pop('current_page', None)
  flash('Войдите в систему под своей учетной записью.')
  return redirect(url_for('login'))

@app.route('/conditions', methods=['GET', 'POST'])
def conditions():
  form = ConditionsFilter()
  stmt = select(models.Conditions)

  if form.validate_on_submit():
    date_from = form.date_from.data
    date_to = form.date_to.data
    location = form.location.data
    comment = form.comment.data

    if date_from:
      stmt = stmt.where(models.Conditions.date > date_from)
    if date_to:
      stmt = stmt.where(models.Conditions.date < date_to)
    if location:
      stmt = stmt.where(models.Conditions.location.like(f'%{location}%'))
    if comment:
      stmt = stmt.where(models.Conditions.comment.like(f'%{comment}%'))

  if not session.get('logged_in'):
    return redirect(url_for('login'))
  if request.method == 'POST':
    filters = {
      'date_from': request.form.get('date_from'),
      'date_to': request.form.get('date_to'),
      'location': request.form.get('location'),
      'comment': request.form.get('comment')
    }

  stmt = stmt.order_by(desc(models.Conditions.date))
  data = db.session.scalars(stmt.limit(Config.RECORDS_LIMIT)).all()
  return render_template('conditions.html', title="Условия поверки",
    username=session.get('username'),
    data = data, form = form)

#if __name__ == "__main__":
#  app.run(debug=True)
