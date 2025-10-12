from flask import Flask, render_template
#from typing import Optional
#from dataclasses import dataclass, field
from DB import getTaskList


app = Flask(__name__)



#lista_tarefas = [["Caminhar no parque", True],["Jogar futebol", False],["Ir ao mercado", True]]
lista_de_tarefas = getTaskList()
'''@dataclass(frozen=False)
class Tarefas:
    nome: str
    concluido: bool
    data_prazo: str
        
lista_tarefas = [
    Tarefas("Caminhar no parque", False, "19/09/2006"),
    Tarefas("Jogar videogame", True, "20/05/2026"),
    Tarefas("Buscar cola", False, "11/09/2001")
]

t1 = lista_tarefas[0]
t2 = lista_tarefas[1]
t3 = lista_tarefas[2]'''




@app.route('/')
def home_pg():
   #return render_template("lista_tarefas.html", tarefas=lista_tarefas)
    return render_template("lista_tarefas.html", tarefas=lista_de_tarefas)

app.run()