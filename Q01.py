import random


arq = open('Lista_nao_ordenada.txt', 'w')
lista = []
i=1
n = int(input("Insira o número de elementos a serem gerados: "))
while i <= n:
    lista.append(random.randint(1,1000000))
    i += 1
lista_str = str(lista).strip('[]')
arq.write(lista_str)
arq.close()
