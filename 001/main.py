

from flask import Flask, render_template,redirect


app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'



@app.route('/')
def home():
    return render_template('login.html')



@app.route('/login')
def login():

    nome = request.from.get('nome')
    senha = request.from.get('senha')

    return redirect('/')

