
import sqlite3
import os


 



def getConnection():
    databaseName="autofrases.db"
    stringConnection="{}/{}".format(os.getcwd(),databaseName)
    conn=sqlite3.connect(stringConnection)
    return conn

# Criar tabela
def create_table():
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS  frases (
                id           INTEGER PRIMARY KEY AUTOINCREMENT,
                frase        TEXT    NOT NULL,
                autor        TEXT    NOT NULL,
                data_criacao TEXT    NOT NULL
            );
     ''')
    conn.commit()


    cursor.execute('''
            CREATE TABLE IF NOT EXISTS  sensor (
                id         INTEGER PRIMARY KEY AUTOINCREMENT,
                dado       INTEGER,
                created_at TEXT
            );
     ''')
    conn.commit()
    conn.close()


def insert_frase(frase, autor,dados):
    conn = getConnection()
    cursor = conn.cursor()
    sql="INSERT INTO frases(frase, autor,data_criacao) VALUES ('"+frase+"','"+autor+"','"+dados+"') "
    cursor.execute(sql)
    conn.commit()
    conn.close()


def insert_dados(dados):
    conn = getConnection()
    cursor = conn.cursor()
    createdAt=str(datetime.datetime.now())
    sql="INSERT INTO sensor(dado,created_at) VALUES ('"+dado+"','"+createdAt+"')"
    cursor.execute(sql)
    conn.commit()
    conn.close()


def total_de_frases():
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT count(*) as qt FROM frases
    ''')
    (number_of_rows,)=cursor.fetchone()
    conn.close()
    return number_of_rows



def frases_limit(linha):
    conn = getConnection()
    cursor = conn.cursor()
    sql="SELECT frase, autor,data_criacao FROM frases limit {},1".format(str(linha))
    cursor.execute(sql)
    result=cursor.fetchone()
    frase_selecionada=normalize('NFKD', result[0]).encode('ASCII', 'ignore').decode('ASCII')
    data={
        "frase":frase_selecionada,
        "autor":result[1],
        "publicado":result[2],
        
    }
    json_str = json.dumps(data,sort_keys=True, indent=4)
    conn.close()

    return json_str




