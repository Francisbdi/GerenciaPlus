import sqlite3

#CRIA O BANCO DE DADOS
banco = sqlite3.connect('principal.db')

#recebe o objeto e usa o metodo cursor para manipular a tabela do banco
cursor = banco.cursor()

#COMANDO PARA A CRIAÇÃO DE UMA TABELA
#cursor.execute("CREATE TABLE users (id INTEGER NOT NULL, login VARCHAR(15) NOT NULL, senha VARCHAR(12) NOT NUll, PRIMARY KEY(id))")
#banco.commit()
#banco.close()

#cursor.execute("CREATE TABLE clientes (id INTEGER, nome VARCHAR(50), endereco VARCHAR(50), telefone VARCHAR(13), tempo VARCHAR(4), estabelecimento VARCHAR(50), tipoestabelecimento VARCHAR(15), PRIMARY KEY(id))")
#banco.commit()
#banco.close()

#cursor.execute("CREATE TABLE barracas (id INTEGER, tipo VARCHAR(5), nome VARCHAR(50), estabelecimento VARCHAR(50), preco INTEGER, status VARCHAR(10))")
#banco.commit()
#banco.close()

cursor.execute("INSERT INTO barracas (tipo, preco, status) VALUES ('A1', 600, 'DISPONIVEL')")
banco.commit()
banco.close()

#cursor.execute("CREATE TABLE fila (id INTEGER, nome VARCHAR(50), estabelecimento VARCHAR(50), tempo varchar(4), status VARCHAR(10), tipo VARCHAR(5))")
#banco.commit()
#banco.close()