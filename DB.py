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

def get_db_connection():
    try:
        conn = psycopg2.connect(dbname=db_name, user=db_user, host=db_host, password=db_pw)
        return conn
    except psycopg2.OperationalError as e:
        print(f"ERRO DE CONEXÃO: {e}")
        return None

def executeQuery(sql_template, params=None, fetch=False):
    with get_db_connection() as conn:
        if conn is None: return []

        with conn.cursor() as cur:
            cur.execute(sql_template, params)

            if not fetch:
                conn.commit()
                return None
            else:
                return cur.fetchall()

def getTaskList():
    sql = 'SELECT ID, nome_task, is_done, data_fim FROM public."TaskList";'
    return executeQuery(sql, fetch=True)

def addTask(nome, data):
    sql = 'INSERT INTO public."TaskList"(nome_task, data_fim) VALUES (%s, %s)'
    executeQuery(sql, (nome, data))

def updateTask(nome, ID):
    sql = 'UPDATE public."TaskList" SET nome_task=%s WHERE ID=%s;'
    executeQuery(sql, (nome, ID))

def deleteTask(ID):
    sql = 'DELETE FROM public."TaskList" WHERE ID=%s;'
    executeQuery(sql, (ID,))

def mudarStatusTask(ID):
    sql =  'UPDATE public."TaskList" SET is_done = NOT is_done WHERE ID = %s;'
    executeQuery(sql, (ID,))