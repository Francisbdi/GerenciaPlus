import PySimpleGUI as sg
from biblioteca import *

#tela que vai aparecer cso esteja disponivel
def Mostra_Disponivel(barraca, pessoa):
    layout = [
        [sg.Text('Código:'), sg.Text(barraca[1])],
        [sg.Text('Tipo:'), sg.Text('Alimento')],
        [sg.Text('Valor:'), sg.Text(barraca[4])],
        [sg.Text('Status:'), sg.Text(barraca[5])],
        [sg.Button('Alugar')]
    ]
    janela = sg.Window('Festa', layout = layout)
    janela.read()