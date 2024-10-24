from Player import Player
import sqlite3
import os

con = sqlite3.connect('masterGamers.db')
cur = con.cursor()

def insertPlayer(player):
    sql_insert = f'insert into Players(nome, email, telefone) values ("{player.getNome()}", "{player.getEmail()}", "{player.getTelefone()}")'
    cur.execute(sql_insert)


def deletePlayer(ID):
    sql_delete = f'delete from Players where ID = {ID}'
    cur.execute(sql_delete)


def consultaOrdem():
    sql_consultaOrdemPlayer = 'SELECT * FROM Players ORDER BY nome ASC'
    resultado = cur.execute(sql_consultaOrdemPlayer)
    for linha in resultado:
        print(linha)


def consultarFiltro(filtro):
    sql_filtro = f'SELECT * from Players WHERE {filtro}'
    resultado = cur.execute(sql_filtro)
    for linha in resultado:
        print(linha)

def menu():
    print("="*20 + "MENU" + "="*20)
    print("[1] INSERIR")
    print("[2] APAGAR")
    print("[3] CONSULTAR")
    print("[4] FILTRO")
    print("[5] SAIR")
    resp = int(input("Digite a opção desejada:"))
    return resp

def main():
    while True:
        resp = menu()
        if resp == 1:
            nome = input("Digite o nome do jogador: ")
            email = input("Digite o email do jogador: ")
            telefone = input("Digite o telefone do jogador: ")
            player = Player(nome, email, telefone)
            insertPlayer(player)
        elif resp == 2:
            id = int(input("Digite o ID do jogador que deseja apagar"))
            deletePlayer(id)
        elif resp == 3:
            consultaOrdem()
        elif resp == 4:
            filtro = input("Digite o filtro que deseja para consultar, *DIGITE CORRETAMENTE DE ACORDO COM AS NORMAS SQL*")
            consultarFiltro(filtro)
        elif resp == 5:
            break
        else:
            print("Opção invalida!!!")




    con.commit()


main()




