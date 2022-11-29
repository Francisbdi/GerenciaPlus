import sqlite3
import PySimpleGUI as sg

#função que serve para dar tchau ao usuário
def MostraAdeus():
    layout2 = [
    [sg.Text('Até a Próxima')]
              ]
    janela2 = sg.Window('Tchau', layout = layout2)
    janela2.read()

def CamposVazios():
    layout3 = [
    [sg.Text('Não pode conter campos vazios')]
              ]
    janela3 = sg.Window('Erro', layout = layout3)
    janela3.read()

def UserInvalido():
    layout4 = [
    [sg.Text('Usuário ou senha inválido')]
              ]
    janela4 = sg.Window('Erro', layout = layout4)
    janela4.read()

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

def cadastrar_cliente(nome, endereco, telefone, participacao, estabelecimento, tipoestabelecimento, usuario, senha):
    conexao = sqlite3.connect('principal.db')
    c = conexao.cursor()

    c.execute("INSERT INTO clientes (nome, endereco, telefone, tempo, estabelecimento, tipoestabelecimento) VALUES (?, ?, ?, ?, ?, ?)", (nome, endereco, telefone, participacao, estabelecimento, tipoestabelecimento))
    c.execute("INSERT INTO users (login, senha) VALUES (?, ?)", (usuario, senha))
    conexao.commit()
    conexao.close()

