import sqlite3
from biblioteca import *
import PySimpleGUI as sg
from Status import *

#Botoes que vão simular os locais
def tela_principal(tupla_dados):
    dados = tupla_dados

    layout = [
        [sg.Text('Seja Bem vindo ' + dados[1])],
        [sg.Text('MAPA DAS BARRACAS!')],
        [sg.Button('A1', size = (10,2)), sg.Button('A2', size = (10,2)), sg.Button('A3', size = (10,2))],
        [sg.Button('B1', size = (10,2)), sg.Button('B2', size = (10,2)), sg.Button('B3', size = (10,2))],
        [sg.Button('R1', size = (10,2)), sg.Button('R2',size = (10,2)), sg.Button('R3', size = (10,2))],
        [sg.Text('Grupo A = Alimentos')],
        [sg.Text('Grupo B = Bebidas')],
        [sg.Text('Grupo R = Roupas')],
        [sg.Text('Para mais informações verifique selecionando o lote.')]
    ]

    janela = sg.Window('GerênciaPlus', layout = layout)    

    while True:
        event, values = janela.read()
        if event == sg.WIN_CLOSED:
            break
        #clicando no botao ele vai jogar o valor do tipo dele em uam variavel 
        if event == 'A1' or 'A2' or 'A3' or 'B1' or 'B3' or 'B3' or 'B1' or 'R2' or 'R3':
            verificador = event
            #verifica na função o tipo dela no banco
            barraca = Verifica_Status(verificador)
            #como o banco retorna uma tupla, é so usar a posição que ela aparece na tupla barraca e o upper() é para deixar tudo maiusculo
            if barraca[5] == 'disponivel'.upper():
                #usa a tupla na função que vai mostrar se ela esta disponivel
                Mostra_Disponivel(barraca, dados)
            elif barraca[5] == 'alugado'.upper():
                #usa a tupla na função que vai mostrar se ela esta alugado
                Mostra_Alugado(barraca, dados)
            elif barraca[5] == 'reservado'.upper():
                #usa a tupla na função que vai mostrar se ela esta reservado
                Mostra_Reservado(barraca, dados)