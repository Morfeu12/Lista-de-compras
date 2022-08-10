from datetime import date
from model.connect import criarlistacompras

lista_compras = criarlistacompras()


def restaurarlistacompras():
    global lista_compras
    lista_compras = criarlistacompras()


def removerprodutos():
    produto_nome = input("Qual produto deseja remover? ")
    if lista_compras.get(produto_nome):
        lista_compras.pop(produto_nome)
    else:
        print("Error: registro não encontrado.\n")


def cadastrarprodutos(produto_nome):
    # usando biblioteca datetime para recuperar a data atual e formatar
    data_atual = date.today().strftime('%d/%m/%Y')
    lista_compras[produto_nome] = [input("Unidade de medida (Kg, g, L, UN ou m): "),
                                   float(input("Quantidade a ser comprada: ")),
                                   False,
                                   data_atual]


def validaritemspendentes():
    # A função list() recupera os .keys ou .values
    new_list_compras = list(lista_compras.keys())
    items_pendentes = []
    for i in range(len(lista_compras)):
        produto_detalhes = lista_compras.get(new_list_compras[i])
        if (produto_detalhes[2] is False) and (produto_detalhes[1] > 0):
            items_pendentes.append(new_list_compras[i])
    return items_pendentes


def mostraritemspendentescompra():
    itemspendentes = validaritemspendentes()
    for i in range(len(itemspendentes)):
        produto_detalhes = lista_compras.get(itemspendentes[i])
        print(str(i + 1) + " - " + itemspendentes[i] + " " + str(round(produto_detalhes[1])) + produto_detalhes[0])


def mostrartodosprodutos():
    new_list_compras = list(lista_compras.keys())
    for i in range(len(lista_compras)):
        produto_detalhes = lista_compras.get(new_list_compras[i])
        if produto_detalhes[2]:
            msg = "Produto comprado."
        else:
            msg = "Pendente compra."
        print(str(i + 1) + " - " + new_list_compras[i] + ", " + str(round(produto_detalhes[1])) + produto_detalhes[
            0] + " | " + msg)


def pesquisarprodutos(produto):
    produto_pesquisado = lista_compras.get(produto)
    if produto_pesquisado is not None:
        print("\nProduto: ", produto)
        print("Unidade de medida: ", produto_pesquisado[0])
        print("Quantidade: ", produto_pesquisado[1])
        if produto_pesquisado[2] is False:
            print("Produto foi comprado? Não")
        else:
            print("Produto foi comprado? Sim")
        return True
    else:
        print("\nO produto \"" + str(produto) + "\" não existe.")
        return False


def atualizarlote(produtos_pendentes):
    for i in range(len(produtos_pendentes)):
        produto_detalhes = lista_compras.get(produtos_pendentes[i])
        lista_compras[produtos_pendentes[i]] = [produto_detalhes[0],
                                                produto_detalhes[1],
                                                True,
                                                date.today().strftime('%d/%m/%Y')]


def atualizarlistadecompras():
    produtos_pendetes = validaritemspendentes()
    x = input("TODOS os produtos listados foram comprados? (\"S\" ou \"N\") ").upper()
    if x == "S":
        atualizarlote(produtos_pendetes)
        print("\nOs produtos foram atualizados para \"COMPRADO\".\n")

    else:
        print("Opção inválida... Tente novamente.")
        atualizarlistadecompras()
