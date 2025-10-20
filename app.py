from flask import Flask, render_template, request, redirect, url_for
from DB import getTaskList, addTask

app = Flask(__name__)

lista_de_tarefas = getTaskList()

@app.route("/")
def home_pg():
    lista_de_tarefas = getTaskList()
    return render_template("lista_tarefas.html", tarefas=lista_de_tarefas)

@app.route("/add", methods=['POST'])
def add():
    nomeTask = request.form['nomeTask']
    dataFim = request.form['dataFim']
    addTask(nomeTask, dataFim)
    return redirect(url_for('home_pg'))

app.run()