import os
import psycopg2
from dotenv import load_dotenv

# carregar as variáveis do .env
load_dotenv()

# atribuir as varíáveis às credenciais
db_name = os.getenv("db_name")
db_user = os.getenv("db_user")
db_host = os.getenv("db_host")
db_pw = os.getenv("db_pw")


def getTaskList():
    conn = psycopg2.connect(dbname=db_name, user=db_user, host=db_host, password=db_pw)
    cur = conn.cursor()
    cur.execute('SELECT nome_task, is_done FROM public."TaskList";')
    lista_de_tarefas = cur.fetchall()
    cur.close
    conn.close
    return lista_de_tarefas

def addTask(nome, data):
    conn = psycopg2.connect(dbname=db_name, user=db_user, host=db_host, password=db_pw)
    cur = conn.cursor()
    cur.execute('INSERT INTO public."TaskList"(nome_task, data_fim) values(\'%s\', \'%s\');commit;' % (nome, data))
    cur.close
    conn.close