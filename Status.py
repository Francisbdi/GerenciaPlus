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
    if barraca[0] ==  dados[0]:
        layout = [
            [sg.Text('Código:'), sg.Text(barraca[1])],
            [sg.Text('Valor:'), sg.Text(barraca[4])],
            [sg.Text('Status:'), sg.Text(barraca[5])],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]
    else:
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
            break
        if event == 'Aguardar':
            Criar_Fila(barraca[1], dados[0], dados[1], dados[5], dados[4])
        
        elif event == "Confirmar":
            status = 'ALUGADO'
            Deleta_Fila(barraca[1])
            Update_Status(barraca[1], dados[0], dados[1], dados[5], status)
        
        elif event == 'Cancelar':
            if Verifica_Fila(barraca[1]) == None:
                status = 'DISPONIVEL'
                id = 'null'
                nome = 'null'
                estabelecimento = 'null'
                Update_Status(barraca[1], id, nome, estabelecimento, status)
            else:
                id = Listar_fila()
                print(id)