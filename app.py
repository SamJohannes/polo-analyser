#!/usr/bin/env python3.5

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import nltk
from sqlalchemy import create_engine
from db.db_url import db_url

    
app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello'

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
