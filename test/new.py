'''
    __name__ = new
    __author__ = 'Kyle Roux'
    __year__ = 2014
'''
from flask import Flask, render_template, flash, request, make_response, session, g, url_for, redirect
from flask.ext.sqlalchemy import SQLAlchemy

def make_app():
    app = Flask(__name__)
    db = SQLAlchemy(app)
    return app

if __name__ == "__main__":
    app = make_app()

    #views 
    @app.route('/')
    def index():
        return render_template('index.html')

    app.run(debug=True,host='0.0.0.0',port=8080)

