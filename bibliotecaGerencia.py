import sqlite3

def Listar_Lotes(verificador):
    con = sqlite3.connect("principal.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM barracas WHERE status = ?", (verificador,))
    lista = cursor.fetchall()
    con.commit()
    con.close()
    somatorio = 0

    for linha in lista:
        print("---------------")
        print('Tipo: ', linha[1])
        print('Nome cliente: ', linha[2])
        print('Estabelecimento: ', linha[3])
        print('Preço: ', linha[4])
        print('Status: ', linha[5])
        somatorio += linha[4]
        
    print("---------------")
    print(f'Soma dos lotes: {somatorio},00')