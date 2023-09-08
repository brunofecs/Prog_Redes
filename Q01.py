import random


arq = open('Lista_nao_ordenada.txt', 'w')
lista = []
i=1

try:
    n = int(input("Insira o número de elementos a serem gerados: "))
    if n > 0:
        while i <= n:
            lista.append(random.randint(1,1000000))
            i += 1
        lista_str = str(lista).strip('[]')
        print('Escrevendo no arquivo...')
        arq.write(lista_str)
    else:
        print('Informe um valor maior que 0.')
except:
    print('Informe um valor númerico.')

arq.close()
