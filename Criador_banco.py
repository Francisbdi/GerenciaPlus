import sqlite3

#CRIA O BANCO DE DADOS
banco = sqlite3.connect('principal.db')

#recebe o objeto e usa o metodo cursor para manipular a tabela do banco
cursor = banco.cursor()

#COMANDO PARA A CRIAÇÃO DE UMA TABELA
#cursor.execute("CREATE TABLE users (id INTEGER NOT NULL, login VARCHAR(15) NOT NULL, senha VARCHAR(12) NOT NUll, PRIMARY KEY(id))")
#banco.commit()
#banco.close()

cursor.execute("CREATE TABLE clientes (id INTEGER, nome VARCHAR(50), endereco VARCHAR(50), telefone VARCHAR(13), tempo VARCHAR(4), estabelecimento VARCHAR(50), tipoestabelecimento VARCHAR(15), PRIMARY KEY(id))")
banco.commit()
banco.close()

cursor.execute("CREATE TABLE barracas (id INTEGER, A1 VARCHAR(1), A2 VARCHAR(1), A3 VARCHAR(1), B1 VARCHAR(1), B2 VARCHAR(1), B3 VARCHAR(1), R1 VARCHAR(1), R2 VARCHAR(1), R3 VARCHAR(1) ")
banco.commit()
banco.close()