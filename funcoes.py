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
        for i in nome_lista: nome_arquivo.write(f'{i}\n')
        boolSucesso = True
        nome_arquivo.close()

    return boolSucesso
