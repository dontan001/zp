# -*- coding: utf-8 -*-

from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', data="abcd")

@app.route('/cat/{id}')
def cat():
    data = range(1, 10)

if __name__ == "__main__":
    app.run()