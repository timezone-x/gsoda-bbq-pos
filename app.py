import sqlite3
from flask import Flask, jsonify, render_template, request, url_for, redirect, session


app = Flask(__name__)
app.secret_key = "8dee4e112d63655ddfd1b4956bd038181175cdea36ea7bc30a484c47a1247013"


def loadPricing():
    with sqlite3.connect('backend.db') as db:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM itemPricing')
        pricing = cursor.fetchall()
        return pricing


def loadTransactions():
    with sqlite3.connect('backend.db') as db:
        cursor = db.cursor()
        cursor.execute('SELECT COUNT(*) FROM transactions')
        transactionCount = cursor.fetchall()
        cursor.execute('SELECT * FROM transactions')
        transactions = cursor.fetchall()
        return transactionCount, transactions


def checkToken(token, lvlReq):
    if lvlReq == 1:
        sql = 'SELECT 1 FROM tokens WHERE token = ? AND expires > DATE("now")'
        lvl = 1
    else:
        sql = 'SELECT 1 FROM tokens WHERE token = ? AND expires > DATE("now") AND perm_level = 2'
        lvl = 2

    with sqlite3.connect('backend.db') as db:
        tokenToCheck = int(token)
        cursor = db.cursor()
        cursor.execute(sql, (tokenToCheck,))
        result = cursor.fetchone()
        print(result)
        if result:
            return True, lvl
        else:
            return False


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/login/<mode>", methods=['POST', 'GET'])
def login(mode):
    if request.method == 'POST':
        name = request.form.get('name')
        token = request.form.get('token')
        print(f"token: {token}")
        if mode == 'pos':
            if checkToken(token, 1):
                session['user'] = name
                session['session'] = True
                session['perm_lvl'] = checkToken(token, 1)[1]
                return redirect('/app/pos')
            else:
                return redirect('/error/failed-login-invalid-token')
        elif mode == 'admin':
            if checkToken(token, 2):
                session['user'] = name
                session['session'] = True
                session['perm_lvl'] = '2'

                return redirect('/app/admin')
            else:
                return redirect('/error/failed-login-invalid-or-wrong-perms-token')

    else:
        return render_template("login.html", mode=mode)


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


@app.route('/app')
def homepage():
    if session.get('session'):
        return render_template('app.html')
    else:
        return "Access Denied", 403


@app.route('/app/pos')
def posApp():
    items = loadPricing()
    return render_template('pos-app.html', items=items)


@app.route('/app/admin')
def adminPage():
    transactionsCount = loadTransactions()[0]
    transactions = loadTransactions()[1]
    return render_template('admin.html', transactions=transactions, transactionsCount=transactionsCount)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@app.route('/error/<posapp_error>')
def error_page(posapp_error):
    return render_template("error.html", app_error=posapp_error)


@app.route('/api/items')
def getItems():
    with sqlite3.connect('backend.db') as db:
        db.row_factory = sqlite3.Row
        cursor = db.cursor()

        cursor.execute('SELECT * FROM itemPricing')
        rows = cursor.fetchall()
        items = [dict(row) for row in rows]
    return jsonify(items)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
