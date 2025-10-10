from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Olá do Flask rodando no Arch Linux (WSL 2)!'