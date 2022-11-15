import sqlite3
import PySimpleGUI as sg

#Cria o layout da tela, sempre pensando em linhas
layout = [
    [sg.Text('Usuário')],
    [sg.Input(key = 'usuario')],
    [sg.Text('Senha')],
    [sg.Input(key = 'senha')],
    [sg.Button('Login'), sg.Button('Cadastrar')],
    [sg.Text('', key = 'mensagem')],
]

#criar uma janela
janela = sg.Window('Login', layout = layout)
events, values = janela.read()

login = values['usuario']
senha = values['senha']

def VerificaLogin(l):
    banco = sqlite3.connect('princial.db')
    cursor = banco.cursor()

    cursor.execute("SELECT * FROM users login == ?",(l))
    pessoa = cursor.fetchone()
    banco.commit()
    banco.close()

    return pessoa