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
        lstRetorno = None
    except FileNotFoundError:
        print('Arquivo não existe, confira e insira novamente!')
        lstRetorno = None
    else:
        for linha in arq_input:
            lstRetorno.append(arq_input.readlines())
        boolSucesso = True

    return boolSucesso, lstRetorno


# ----------------------------------------------------------------------
def ordena_bubble(nome_lista: list):
    boolSucesso = False
    lstOrdenada = None



    return boolSucesso, lstOrdenada

# ----------------------------------------------------------------------
def ordena_insertion(nome_lista: list):
    boolSucesso = False
    lstOrdenada = None



    return boolSucesso, lstOrdenada

# ----------------------------------------------------------------------
def ordena_selection(nome_lista: list):
    boolSucesso = False
    lstOrdenada = None



    return boolSucesso, lstOrdenada

# ----------------------------------------------------------------------
def ordena_quick(nome_lista: list):
    boolSucesso = False
    lstOrdenada = None



    return boolSucesso, lstOrdenada

# ----------------------------------------------------------------------
def ordena_lista(nome_lista: str, metodo_ordena: str):
    boolSucesso = False
    lstRetorno = None



    return boolSucesso, lstRetorno
