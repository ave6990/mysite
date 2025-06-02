from flask import render_template, flash, redirect, url_for, session, request
from app import app, db
import app.models as m
from sqlalchemy import select, desc
from config import Config

@app.route('/')
@app.route('/index')
def index():
  if not session.get('logged_in'):
    return redirect(url_for('auth.login'))
  return render_template('index.html', title="Поверки",
    username=f"{session.get('username')}",
    content='Hello from Flask!')

#if __name__ == "__main__":
#  app.run(debug=True)
