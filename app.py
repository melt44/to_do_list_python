from flask import Flask, render_template, request, redirect, url_for
from DB import getTaskList, addTask, updateTask, deleteTask, mudarStatusTask

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

@app.route("/update", methods=['POST'])
def update():
    nomeTaskAtualizada = request.form['updateTask']
    id = request.form['ID']
    button = request.form['saveOrDelete']
    if button == 'save':
        updateTask(nomeTaskAtualizada, id)
    elif button == 'X':
        deleteTask(id)
    return redirect(url_for('home_pg'))

@app.route("/status_feito", methods=['POST'])
def status_feito():
    try:
        task_id = int(request.form['ID'])
        mudarStatusTask(task_id)
    except ValueError:
        print("ERRO: ID da tarefa inválido.")
    
    return redirect(url_for('home_pg'))


app.run()