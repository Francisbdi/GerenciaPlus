import PySimpleGUI as sg
from biblioteca import *

#tela que vai aparecer cso esteja disponivel
def Mostra_Disponivel(barraca, tupla_dados):
    dados = tupla_dados
    layout = [
        [sg.Text('Código:'), sg.Text(barraca[1])],
        [sg.Text('Valor:'), sg.Text(barraca[4])],
        [sg.Text('Status:'), sg.Text(barraca[5])],
        [sg.Button('Alugar'), sg.Button('Reservar')]
    ]
    janela = sg.Window('Festa', layout = layout)
    
    while True:
        event, values = janela.read()

        if event == sg.WIN_CLOSED:
            MostraAdeus()
            break
        if event == 'Alugar':
            Update_Status(barraca[1], dados[0], dados[1], dados[5])
        if event == 'Reservar':
            pass