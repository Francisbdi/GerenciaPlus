import sqlite3
import PySimpleGUI as sg

#função que serve para dar tchau ao usuário
def MostraAdeus():
    layout2 = [
    [sg.Text('Até a Próxima')]
              ]
    janela2 = sg.Window('Tchau', layout = layout2)
    janela2.read()

def VerificaVazio(valor):
    if len(valor) == 0:
        return 0


#função para verificar se o login e senha que foi passado existe no banco 
def Verifica_Login(l):
    con = sqlite3.connect('principal.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM users WHERE login = ?", (l))
    pessoa = cursor.fetchone()   
    con.commit()
    con.close()

    if pessoa != None:
        return pessoa
    else:
        return None
