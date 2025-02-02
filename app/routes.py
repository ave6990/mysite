# A very simple Flask Hello World app for you to get started with...

from flask import render_template 
from app import app

@app.route('/')
def home():
  return render_template('index.html', content='Hello from Flask!')

@app.route('/login')
def login():
  return render_template('login.html')

#if __name__ == "__main__":
#  app.run(debug=True)
