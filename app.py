
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chervi')
def chervi():
    return render_template('chervi.html')

@app.route('/face')
def face():
    return render_template('face.html')

@app.route('/sky')
def sky():
    return render_template('sky.html')

@app.route('/patsany')
def patsany():
    return render_template('patsany.html')

if __name__ == '__main__':
    app.run(debug=True)