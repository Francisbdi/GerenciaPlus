import sqlite3
import PySimpleGUI as sg

#CRIA A TELA DE CADASTRO 
layout = [
    [sg.Text('Nome')],
    [sg.Input(key = 'nome')],
    [sg.Text('Endereco')],
    [sg.Input(key = 'endereco')],
    [sg.Text('Telefone')],
    [sg.Input(key = 'telefone')],
    [sg.Text('Primeira Participação')],
    [sg.Input(key = 'tempo')],
    [sg.Text('Nome do estabelecimento')],
    [sg.Input(key = 'estabelecimento')],
    [sg.Radio('Roupas', "Radio1", default = False, key = 'tipo1'), sg.Radio('Comidas', "Radio1", default = False, key = 'tipo2'),
    sg.Radio('Artesanatos', "Radio1", default = False, key ='tipo3')],
    [sg.Text('Usuário')],
    [sg.Input(key = 'usuario')],
    [sg.Text('Senha')],
    [sg.Input(key = 'senha')],
         ]
#OBS: ACESSAR LINK PARA ENTENDER O sg.Radio https://holypython.com/gui-with-python-checkboxes-and-radio-buttons-pysimplegui-part-ii/

janela = sg.Window('Cadastro', layout = layout)

janela.read()