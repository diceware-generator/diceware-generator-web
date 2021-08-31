from flask import Flask, render_template
import random, sys


app = Flask(__name__)

@app.route("/")
def index():
    diceware_password = get_diceware()
    return render_template('index.html', message=diceware_password)

def get_diceware():
    w = 'dict/dicionario-pt-low.txt')]
    return ' '.join(random.SystemRandom().choice(w) for i in range(6))