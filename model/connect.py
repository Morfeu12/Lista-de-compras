import ast
from datetime import datetime


# Dados de origem file.txt
def carregararquivo():
    try:
        arquivo = open('model/db_shoppinglist.txt', 'r+')
        # arquivo = open('db_shoppinglist.txt', 'r+')
    except FileNotFoundError:
        nomearquivotemp = "TEMP_db_"+str(datetime.today().strftime('%Y%m%d_%H%M%S'))
        arquivo = open(nomearquivotemp, 'w+')
        print("O arquivo de origem não foi encontrado.\n"
              "Foi criado o arquivo \"TEMP_db_data_horario.txt\" com os dados.")
    return arquivo


def lerarquivo():
    arquivo = carregararquivo()
    texto = arquivo.readlines()
    arquivo.close()
    return texto


def salvararquivo(dados):
    arquivo = carregararquivo()
    arquivo.truncate(0)
    arquivo.writelines(str(dados))
    arquivo.close()


def criarlistacompras():
    # Usa uma função para ler o arquivo.txt que retorna uma lista.
    # Essa lista é tranformada em String e removido os caracteres [" e "] para ficar no padrão de dicionário
    # Depois a String (str) é convertida em dicionário (dict) com a função nativa AST
    lista_compras = ast.literal_eval(str(lerarquivo()).strip('[""]'))
    return lista_compras
