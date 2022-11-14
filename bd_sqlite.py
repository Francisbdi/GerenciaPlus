import sqlite3

banco = sqlite3.connect('principal.db')

cursor = banco.cursor()

cursor.execute("CREATE TABLE usuarios (id INTEGER, login VARCHAR(15) NOT NULL, senha VARCHAR(15) NOT NULL, PRIMARY KEY (id))")
banco.commit()
banco.close()
