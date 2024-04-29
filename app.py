from flask import Flask, render_template, request
from datetime import datetime
import random
from hashlib import sha256

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('portfoiliowebsite.html')

if __name__ == '__main__':
    app.run(debug=True)