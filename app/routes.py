import os



from app import app
from flask import render_template, flash, redirect, url_for, request, session


from flask_wtf.csrf import generate_csrf
from flask_wtf.csrf import CSRFProtect


# -------------------- Routes --------------------
@app.route('/')
@app.route('/index')
def index():
  return render_template('index.html')