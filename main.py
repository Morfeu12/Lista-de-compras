from view.controller_Interface import *
from model.connect import *
from model.list_functions import *

programaExc = True
home()

while programaExc:
    op = menuprincipallayout()
    controlerepeticao = True
    match op:
        case "1":

            while controlerepeticao:
                separador()
                produto_nome = input("Nome do produto: ").capitalize()
                cadastrarprodutos(produto_nome)
                controlerepeticao = repetirfuncao()
            programaExc = continuaruso()
        case "2":
            while controlerepeticao:
                atualizarlistadecomprasfluxo()
                controlerepeticao = repetirfuncao()
            programaExc = continuaruso()
        case "3":
            while controlerepeticao:
                separador()
                removerprodutos()
                controlerepeticao = repetirfuncao()
            programaExc = continuaruso()
        case "4":
            while controlerepeticao:
                separador()
                produto_nome = input("Nome do produto: ").capitalize()
                pesquisarprodutos(produto_nome)
                controlerepeticao = repetirfuncao()
            programaExc = continuaruso()
        case "5":
            mostraritemspendentescompra()
            programaExc = continuaruso()
        case "6":
            separador()
            mostrartodosprodutos()
            programaExc = continuaruso()
        case "7":
            separador()
            restaurarlistacompras()
            programaExc = continuaruso()
        case "8":
            salvararquivo(lista_compras)
            programaExc = continuaruso()
        case "0":
            programaExc = False
        case _:
            separador()
            print("Opção inválida... :(")
            x = input("Aperte qualquer tecla para tente novamente ou \"X\" para sair.: ").upper()
            if x == "X":
                programaExc = False


salvaroudescartar()

