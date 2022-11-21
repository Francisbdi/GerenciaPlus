import sqlite3
from biblioteca import *
from Cadastro import *
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
#loop de eventos, ainda não descobrimos um jeito de não ser com while true
while True:
    #pega os valores e eventos digitados e clicados na janela
    event, values = janela.read()
    
    #se o evento for fechar a janela ele vai chamar a funçaõ de dar tchau
    if event == sg.WIN_CLOSED:
       MostraAdeus()
       break
    
    #se for o elento do botão login ele vai pegar os dados digitados e verficar se está no banco
    elif event == 'Login':
        login = values['usuario']
        senha = values['senha']

        if VerificaVazio(login) != 0:
    
            #se o retorno do banco for igual a vazio entao ele mostra mensagem de erro
            if Verifica_Login(login) == None:
                 janela['mensagem'].update('Usuário ou senha incorreto!')
            else:
                pessoa = Verifica_Login(login)
                id = pessoa[0]
                LoginFeito = pessoa[1]
                SenhaFeito = pessoa[2]
          
                if SenhaFeito == senha:
                    print ("ok")
                else:
                    janela['mensagem'].update('Usuário ou senha incorreto!')
        else:
            janela['mensagem'].update('Usuário ou senha incorreto!')
    elif event == 'Cadastrar':
        TelaCadastro()