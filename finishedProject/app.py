import sqlite3
import os
from FDataBase import FDataBase
from flask import Flask, render_template, url_for, request, flash, g, redirect, abort
from werkzeug.security import generate_password_hash, check_password_hash


DATABASE = 'flsite.db'
DEBUG = True
SECRET_KEY = 'euorhgudfv%$%hnjdfv8j6y4723hr'


app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flsite.db')))


def connect_db():
    connect = sqlite3.connect(app.config['DATABASE'])
    connect.row_factory = sqlite3.Row
    return connect


def create_db():
    """Function to create database"""
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():
    """Connection with DB"""
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.teardown_appcontext
def close_db(error):
    """Close connection"""
    if hasattr(g, 'link_db'):
        g.link_db.close()

@app.route('/')
def index():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('index.html', menu=dbase.getMenu())


@app.route('/login')
def login():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('login.html', menu=dbase.getMenu(), title='Authorization')


@app.route('/register', methods=['POST', 'GET'])
def register():
    db = get_db()
    dbase = FDataBase(db)
    if request.method == 'POST':
        if len(request.form['name']) > 3 and len(request.form['email']) > 5 \
                and len(request.form['psw']) > 3 and request.form['psw'] == request.form['psw2']:
            hash = generate_password_hash(request.form['psw'])
            res = dbase.addUser(request.form['name'], request.form['email'], hash)
            if res:
                flash("You have successfully registered")
                return redirect(url_for('login'))
            else:
                flash("You have some problem. Please, try again", "error")
        else:
            flash("Fields filled in incorrectly")
    return render_template('register.html', menu=dbase.getMenu(), title='Registration')



if __name__ == '__main__':
    app.run(debug=True)
