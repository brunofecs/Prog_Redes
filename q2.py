import funcoes

nome_arq = str(input('Insira o nome do arquivo a ser lido: '))
conteudo = funcoes.ler_arquivo(nome_arq)
lista_ordenada = []
print(conteudo[1])
if conteudo[0]:
    try:
        metodo = str(input('Métodos disponiveis:\nBUBBLE\nINSERTION\nSELECTION\nQUICK\nInsira o método de ordenaçao para a lista gerada: ')).upper
    except:
        print('Erro desconhecido.')

    else:
        if metodo == BUBBLE:
            lista_ordenada = ordena_bubble(conteudo[1])
        elif metodo == INSERTION:
            lista_ordenada = ordena_insertion(conteudo[1])
        elif metodo == INSERTION:
            lista_ordenada = ordena_selection(conteudo[1])
        elif metodo == INSERTION:
            lista_ordenada = ordena_quick(conteudo[1])
        else:
            print('Método de ordenação inválido, insira um método valido!')