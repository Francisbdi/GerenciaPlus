import sqlite3

#CRIA O BANCO DE DADOS
banco = sqlite3.connect('principal.db')

#recebe o objeto e usa o metodo cursor para manipular a tabela do banco
cursor = banco.cursor()

#COAMNDO PARA A CRIAÇÃO DE UMA TABELA
cursor.execute("CREATE TABLE users (id INTEGER NOT NULL, login VARCHAR(15) NOT NULL, senha VARCHAR(12) NOT NUll, PRIMARY KEY(id))")
banco.commit()
banco.close()