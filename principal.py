import sqlite3
from biblioteca import *
import PySimpleGUI as sg

def tela_principal():
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