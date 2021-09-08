from flask import Flask, render_template
from flask_cors import CORS, cross_origin
import random, sys

def get_diceware():
    w = [s.split()[0] for s in open('dict/dicionario-pt-low.txt')]
    return ' '.join(random.SystemRandom().choice(w) for i in range(6))

app = Flask(__name__)
CORS(app, support_credentials=False)

@app.route("/")
@cross_origin()
def index():
    return render_template('index.html')

@app.route("/api/get-diceware")
@cross_origin()
def api_diceware():
    return get_diceware()

@app.route("/health-check")
def health_check():
    return ('Ok')