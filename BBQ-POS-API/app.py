import json
from re import escape
from zlib import decompressobj
from flask import Flask, jsonify

with open("configs.json", "r", encoding="utf-8") as f:
    configs = json.load(f)

snagPrice = configs["pricing"]["snag-price"]
drinkPrice = configs["pricing"]["drink-price"]

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Index Page"


@app.route("/pricing-fetch")
def pricing_fetch():
    return jsonify({
        "snag-price": snagPrice,
        "drink-price": drinkPrice
    })
