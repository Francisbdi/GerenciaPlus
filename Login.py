import sqlite3
from biblioteca import *
from Cadastro import *
import PySimpleGUI as sg

#Cria o layout da tela, sempre pensando em linhas
layout = [
    [sg.Text('Usuário')],
    [sg.Input(key = 'usuario')],
    [sg.Text('Senha')],
    [sg.Input(key = 'senha', password_char='*')],
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

        #verifica se estátudo preenchido
        if VerificaVazio(login)!= 0 and VerificaVazio(senha) !=0:
    
            #se o retorno do banco for igual a vazio entao ele mostra mensagem de erro
            if Verifica_Login(login) == None:
                 UserInvalido()
            else:
                pessoa = Verifica_Login(login)
                id = pessoa[0]
                LoginFeito = pessoa[1]
                SenhaFeito = pessoa[2]
          
                if SenhaFeito == senha:
                    janela['mensagem'].update('Login feito com sucesso!')
                else:
                    #se a senha estiver errada ele mostra o aviso
                    UserInvalido()
        else:
            #se um campo não estiver preenchido ele mosta a menmsagem
            CamposVazios()
    elif event == 'Cadastrar':
        TelaCadastro()
