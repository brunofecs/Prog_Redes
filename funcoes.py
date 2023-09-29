import random, os, sys

DIRATUAL = os.path.dirname(os.path.abspath(__file__))

# ----------------------------------------------------------------------
def gerar_lista(quantidade:int, valor_minimo:int=1, valor_maximo:int=1000000):
    boolSucesso = False
    lstRetorno  = None
    try:
        lstRetorno = [random.randint(valor_minimo, valor_maximo) for _ in range(quantidade)]
    except:
        print(f'\nERRO DESCONHECIDO: {sys.exc_info()[0]}')
    else:
        boolSucesso = True

    return boolSucesso, lstRetorno


# ----------------------------------------------------------------------
def salvar_lista(nome_lista: list, nome_arquivo: str):
    boolSucesso  = False
    nome_arquivo = DIRATUAL + '\\' + nome_arquivo

    try:
        arq_output = open(nome_arquivo, 'w')
    except:
        print(f'\nERRO DESCONHECIDO: {sys.exc_info()[0]}')
    else:
        for i in nome_lista: arq_output.write(f'{i}\n')
        boolSucesso = True
        arq_output.close()

    return boolSucesso


# ----------------------------------------------------------------------
def ler_arquivo(nome_arquivo: str):
    boolSucesso = False
    lstRetorno = []
    try:
        arq_input = open(nome_arquivo, 'r')
    except NameError:
        lstRetorno = none
    else:
        lstRetorno.append(arq_input.read())
        boolSucesso = True

    return boolSucesso, lstRetorno
