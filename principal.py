import sqlite3
from biblioteca import *
import PySimpleGUI as sg
from Status import *

#Botoes que vão simular os locais
def tela_principal(tupla_dados):
    dados = tupla_dados

    layout = [
        [sg.Button('A1', button_color=('black', 'green')), sg.Button('A2'), sg.Button('A3')],
        [sg.Button('B1'), sg.Button('B2'), sg.Button('B3')],
        [sg.Button('R1'), sg.Button('R2'), sg.Button('R3')]
    ]

    janela = sg.Window('Festa', layout = layout)

    while True:
        event, values = janela.read()
        if event == sg.WIN_CLOSED:
            MostraAdeus()
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
            elif barraca[5]:
                print('ok')