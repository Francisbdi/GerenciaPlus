import PySimpleGUI as sg
from bibliotecaGerencia import *

layout = [
    [sg.Text('Gerador de relatórios!')],
    [sg.Text('Lotes Disponíveis:  '), sg.Button('Disponível')],
    [sg.Text('Lotes Alugados:    '), sg.Button('Alugado')],
    [sg.Text('Lotes Reservados: '), sg.Button('Reservado')],
    [sg.Button('Sair')]
]

janela = sg.Window('Gerenciador', layout = layout)

while True:
    event, values = janela.read()

    if event == sg.WIN_CLOSED or event == 'Sair':
        break
    elif event == 'Disponível':
        verificador = 'DISPONIVEL'
        Listar_Lotes(verificador)
    elif event == 'Alugado':
        verificador = 'ALUGADO'
        Listar_Lotes(verificador)
    elif event == 'Reservado':
        verificador = 'RESERVADO'
        Listar_Lotes(verificador)
