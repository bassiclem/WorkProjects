import random

from flask import Flask, render_template, request, jsonify
from market import *
from encoder_RSA import *
from donnees import *
from word2hexa import *

D = Donnees(10011001)
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/test')
def index_test():
    return D.chaine_str


@app.route('/', methods=['POST'])
def read_index_donnees():
    print("running stuff")
    print(request.form['d_in'])
    D.chaine_str = request.form['d_in']
    i = 0
    for_mat = []
    while i < len(D.chaine_str):
        j = random.randint(1, len(D.chaine_str))
        i += j
        for_mat.append(i)

    result = str(D.sequencage(3, 2,3,2 ))
    return result

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
