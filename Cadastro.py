import sqlite3
import biblioteca
import PySimpleGUI as sg


#CRIA A TELA DE CADASTRO 
def TelaCadastro():
    layout = [
    [sg.Text('Nome')],
    [sg.Input(key = 'nome')],
    [sg.Text('Endereco')],
    [sg.Input(key = 'endereco')],
    [sg.Text('Telefone')],
    [sg.Input(key = 'telefone')],
    [sg.Text('Primeira Participação')],
    [sg.Input(key = 'tempo')],
    [sg.Text('Nome do estabelecimento')],
    [sg.Input(key = 'estabelecimento')],
    [sg.Radio('Roupas', "Radio1", default = False, key = 'tipo1'), sg.Radio('Bebidas', "Radio1", default = False, key = 'tipo2'), sg.Radio('Alimentos', "Radio1", default = False, key ='tipo3')],
    [sg.Text('Usuário')],
    [sg.Input(key = 'usuario')],
    [sg.Text('Senha')],
    [sg.Input(key = 'senha', password_char='*')],
    [sg.Button('Cadastrar')],
    [sg.Text('', key = 'mensagem')]
         ]
#OBS: ACESSAR LINK PARA ENTENDER O sg.Radio https://holypython.com/gui-with-python-checkboxes-or-radio-buttons-pysimplegui-part-ii/
    janela = sg.Window('Cadastro', layout = layout)
    while True:
        event, values = janela.read()

        if event == sg.WIN_CLOSED:
            break
        #assim que clicar no botão cadastrar ele vai pegar os campos preenchidos e jogar nas variaveis
        elif event == 'Cadastrar':
            nome = values['nome']
            endereco = values['endereco']
            telefone = values['telefone']
            participacao = values['tempo']
            estabelecimento = values['estabelecimento']
            tipo1 = values['tipo1']
            tipo2 = values['tipo2']
            tipo3 = values['tipo3']
            login = values['usuario']
            senha = values['senha']

            #garante que todas as variaveis vao ser preeenchidas
            if len(nome) !=0 and len(endereco) !=0 and len(telefone) !=0 and len(participacao) !=0 and len(estabelecimento) !=0 and len(login) !=0 and len(senha) !=0: 
                    #caso esteja tudo ok ele vai verificar se foi marcado um dos tipos 
                if tipo1 == True:
                    tipo1 = 'Roupas'
                    if biblioteca.Verifica_Login(login) != None:
                        biblioteca.UserInvalido()
                    else:
                        biblioteca.cadastrar_cliente(nome, endereco, telefone, participacao, estabelecimento, tipo1, login, senha)
                        janela.close()
                elif tipo2 == True:
                    tipo2 = 'Bebidas'
                    if biblioteca.Verifica_Login(login)!= None:
                        biblioteca.UserInvalido()
                    else:
                        biblioteca.cadastrar_cliente(nome, endereco, telefone, participacao, estabelecimento, tipo2, login, senha)
                        janela.close()
                elif tipo3 == True:
                    tipo3 = 'Alimentos'
                    if biblioteca.Verifica_Login(login) != None:
                        biblioteca.UserInvalido()
                    else:
                        biblioteca.cadastrar_cliente(nome, endereco, telefone, participacao, estabelecimento, tipo3, login, senha)
                        janela.close()
                else:
                    janela['mensagem'].update('Escolha um tipo!')
            else:
                biblioteca.CamposVazios()