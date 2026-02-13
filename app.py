from os import name
import sqlite3
from flask import Flask, render_template, request, url_for, redirect


app = Flask(__name__)


# db = sqlite3.connect('backend.db')
# cursor = db.cursor()


def loadPricing():

    db = sqlite3.connect('backend.db')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM items')
    pricing = cursor.fetchall()


def loadTokens():
    db = sqlite3.connect('backend.db')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM tokens')
    validTokens = cursor.fetchall()


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/login/<mode>", methods=['POST', 'GET'])
def login(mode):
    if request.method == 'POST':
        name = request.form['name']
        token = request.form['token']
        validTokens = loadTokens()
        if token in validTokens:
            pass
        else:
            return 'Failed to login, invalid token!'
    else:
        return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)
