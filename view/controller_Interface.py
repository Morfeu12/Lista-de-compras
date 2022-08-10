from model.connect import *
from model.list_functions import *


def separador():
    print('------------------------------------------------')


def home():
    print("==========================================================\n"
          "                     LISTA DE COMPRAS                     \n"
          "By:Omar Costa - https://www.linkedin.com/in/omarcosta152/ \n"
          "==========================================================")


def menuprincipallayout():
    print("[1] Novo produto \n"
          "[2] Atualizar produto \n"
          "[3] Remover produto \n"
          "[4] Pesquisar produto \n"
          "[5] Exibir lista (items pendentes compra) \n"
          "[6] Exibir todos \n"
          "[7] Recarregar dados (Descarta alterações) \n"
          "[8] Salvar alterações \n"
          "[0] Sair")
    return input("\nDigite o número para iniciar a função: ")


def continuaruso():
    separador()
    print("[V] Voltar menu principal.\n"
          # "[S] Salvar alterações.\n"
          "[E] Encerrar programa")
    op = input("\nDigite a opção desejada..: ").upper()
    return controlecontinuar(op)


def repetirfuncao():
    separador()
    repetir = None
    x = input("Executar novamente? (\"S\" or \"N\")").upper()
    if x == "S":
        repetir = True
    elif x == "N":
        repetir = False
    else:
        print("Opss! Opção inválida...")
        repetirfuncao()
    return repetir


def controlecontinuar(op):
    if op == "V":
        separador()
        return True
    elif op == "E":
        return False
    # elif op == "S":
    #     salvararquivo(lista_compras)
    #     print("Lista salva...")
    #     separador()
    #     return True
    else:
        print("Opção invalida ... ")
        continuaruso()


def salvaroudescartar():
    separador()
    op = input("Salvar as alterações? (\"S\" ou \"N\")").upper()
    if op == "S":
        salvararquivo(lista_compras)
        print("Alterações salvas!")
    elif op == "N":
        print("Alterações descartadas.")
    else:
        print("Opção inválida. Tente novamente...")
        salvaroudescartar()
    print("Obrigado por usar nossa solução! Até a próxima! :)")


def listarpesquisadeprodutos():
    separador()
    pesquisar_produto = []
    continuar_pesquisando = "S"
    while continuar_pesquisando == "S":
        pesquisar_produto.append(input("Nome do produto: ").capitalize())
        continuar_pesquisando = input("Pesquisar outro produto (\"S\" ou \"N\")?").upper()
    return pesquisar_produto


def atualizarlistadecomprasfluxo():
    mostraritemspendentescompra()
    separador()
    print("[B] Baixa dos produtos comprados.\n"
          "[E] Editar informações (individual)\n")
    x = input("Digite a opção..: ").upper()
    if x == "B":
        atualizarlistadecompras()
    elif x == "E":
        separador()
        y = input("Nome do produto..: ")
        atualizaratributos(y)
    else:
        print("Ops, essa opção não existe.")
        atualizarlistadecomprasfluxo()


def atualizaratributos(produto):
    x = pesquisarprodutos(produto)
    separador()
    if x:
        cadastrarprodutos(produto)
    separador()
