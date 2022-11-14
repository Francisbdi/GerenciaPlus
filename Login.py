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
janela.read()