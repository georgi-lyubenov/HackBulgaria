from flask import Flask
import jinja2
from flask import render_template
app = Flask(__name__)
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from create_db import *


@app.route('/')
def get():
    return render_template('index.html', links="")

@app.route('/search/')
def search():
    searchword = request.args.get('search_word', '')
    engine = create_engine("sqlite:///my_database.db")
    session = Session(bind=engine)
    #conn = sqlite3.connect("my_database.db")
    #cursor = conn.cursor()
    #result = cursor.execute('''SELECT URl FROM Website WHERE title LIKE ?''' (('%' + searchword + '%'), ))
    result = session.query(Website.URL).filter(Website.title.like('%' + searchword + '%')).all()
    return render_template('index.html', links=result)

if __name__ == '__main__':
    app.debug = True
    app.run()
