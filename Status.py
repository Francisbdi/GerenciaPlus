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
            status = 'ALUGADO'
            Update_Status(barraca[1], dados[0], dados[1], dados[5], status)
        elif event == 'Reservar':
            status = 'RESERVADO'
            Update_Status(barraca[1], dados[0], dados[1], dados[4], status)

#tela que vai aparecer cso esteja disponivel
def Mostra_Alugado(barraca, tupla_dados):
    dados = tupla_dados
    layout = [
        [sg.Text('Código:'), sg.Text(barraca[1])],
        [sg.Text('Valor:'), sg.Text(barraca[4])],
        [sg.Text('Status:'), sg.Text(barraca[5])],
    ]
    janela = sg.Window('Festa', layout = layout)
    janela.read()

def Mostra_Reservado(barraca, tupla_dados):
    dados = tupla_dados
    layout = [
        [sg.Text('Código:'), sg.Text(barraca[1])],
        [sg.Text('Valor:'), sg.Text(barraca[4])],
        [sg.Text('Status:'), sg.Text(barraca[5])],
        [sg.Button('Aguardar')]
    ]
    janela = sg.Window('Festa', layout = layout)
    
    while True:
        event, values = janela.read()

        if event == sg.WIN_CLOSED:
            MostraAdeus()
            break
        if event == 'Aguardar':
            status = 'AGUARDANDO'
            pass