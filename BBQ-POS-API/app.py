import json
import sqlite3
from re import escape
from zlib import decompressobj
from flask import Flask, jsonify

with open("configs.json", "r", encoding="utf-8") as f:
    configs = json.load(f)

snagPrice = configs["pricing"]["snag-price"]
drinkPrice = configs["pricing"]["drink-price"]

app = Flask(__name__)
db = sqlite3.connect("BBQ-POS.db")
cursor = db.cursor()


@app.route("/")
def hello_world():
    return "Index Page"


@app.route("/pricing-fetch")
def pricing_fetch():
    return jsonify({
        "snag-price": snagPrice,
        "drink-price": drinkPrice
    })


@app.route("/transaction<int:with><int:without><int:drinks><donation>")
def transaction(with , without, drinks):
    sql = "INSERT INTO transactions (with, without, drinks, donation, total)"
    cursor.execute()
