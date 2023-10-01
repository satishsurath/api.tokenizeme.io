import os


from flask import Flask
from config import Config
from flask_session import Session
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config.from_object(Config)


# Initialize the session
Session(app)

#Initialize CSFR Protect
csrf = CSRFProtect(app)

from app import routes
