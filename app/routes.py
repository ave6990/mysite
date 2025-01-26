# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html', content='Hello from Flask!')

@app.route('/login')
def login():
  return render_template('login.html')

if __name__ == "__main__":
  app.run(debug=True)
