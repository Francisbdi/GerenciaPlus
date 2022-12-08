import sqlite3
import PySimpleGUI as sg

#função que serve para dar tchau ao usuário
def MostraAdeus():
    layout2 = [
    [sg.Text('Até a Próxima')]
              ]
    janela2 = sg.Window('Tchau', layout = layout2)
    janela2.read()

#função que avisa que não pode ter campos vazios
def CamposVazios():
    layout3 = [
    [sg.Text('Não pode conter campos vazios')]
              ]
    janela3 = sg.Window('Erro', layout = layout3)
    janela3.read()

#função que avisa que o usuario ou a senha estão errados
def UserInvalido():
    layout4 = [
    [sg.Text('Usuário ou senha inválido')]
              ]
    janela4 = sg.Window('Erro', layout = layout4)
    janela4.read()

#função de verificar se o campo está vazio
def VerificaVazio(valor):
    if len(valor) == 0:
        return 0


#função para verificar se o login e senha que foi passado existe no banco 
def Verifica_Login(l):
    con = sqlite3.connect('principal.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM users WHERE login = ?",(l,))
    pessoa = cursor.fetchone()   
    con.commit()
    con.close()

    if pessoa != None:
        return pessoa
    else:
        return None

def pega_pessoa(id):
    con = sqlite3.connect('principal.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM clientes WHERE id = ?",(id,))
    pessoa = cursor.fetchone()   
    con.commit()
    con.close()

    return pessoa
    
#função de cadastrar cliente
def cadastrar_cliente(nome, endereco, telefone, participacao, estabelecimento, tipoestabelecimento, usuario, senha):
    conexao = sqlite3.connect('principal.db')
    c = conexao.cursor()

    c.execute("INSERT INTO clientes (nome, endereco, telefone, tempo, estabelecimento, tipoestabelecimento) VALUES (?, ?, ?, ?, ?, ?)", (nome, endereco, telefone, participacao, estabelecimento, tipoestabelecimento))
    c.execute("INSERT INTO users (login, senha) VALUES (?, ?)", (usuario, senha))
    conexao.commit()
    conexao.close()

#função para verificar o status no banco passando como parametro o seu tipo
def Verifica_Status(verificador):
    con = sqlite3.connect('principal.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM barracas WHERE tipo = ?",(verificador,))
    barraca = cursor.fetchone()   
    con.commit()
    con.close()

    return barraca

def Update_Status(verificador, id, nome, estabelecimento, status):
    con = sqlite3.connect('principal.db')
    cursor = con.cursor()
    cursor.execute("UPDATE barracas SET id = ?, nome = ?, estabelecimento = ?, status = ? WHERE tipo = ?",(id, nome, estabelecimento, status, verificador)) 
    con.commit()
    con.close()

def Criar_Fila(verificador, id, nome, estabelecimento, tempo):
    con = sqlite3.connect('principal.db')
    cursor = con.cursor()
    cursor.execute("INSERT INTO fila (id, nome, estabelecimento, tempo, tipo) VALUES (?,?,?,?,?)", (id, nome, estabelecimento, tempo, verificador)) 
    con.commit()
    con.close()

def Deleta_Fila(verificador):
    con = sqlite3.connect("principal.db")
    cursor = con.cursor()
    cursor.execute("DELETE FROM fila WHERE tipo = ?", (verificador,))
    con.commit()
    con.close()

def Verifica_Fila(verificador):
    con = sqlite3.connect('principal.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM fila WHERE tipo = ?",(verificador,))
    barraca = cursor.fetchone()   
    con.commit()
    con.close()

    return barraca

def Listar_fila():
    con = sqlite3.connect("principal.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM fila;")
    fila = cursor.fetchall()
    con.commit()
    con.close()

    maisTempo = 9999

    for linha in fila:
        if int(linha[3]) < maisTempo:
            maisTempo = int(linha[3])
            id = linha[0]
            return