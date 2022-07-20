# 1. Ordem Crescente. Escreva um programa Python que leia números inteiros (do usuário) e os
# armazena em uma lista. Seu programa deve continuar lendo inteiros até que o usuário entre
# com o valor 0 (zero). Então, o programa deve exibir em ordem crescente todos os números
# digitados pelo usuário sem incluir o valor 0, com um valor em cada linha impressa. Obs.: você
# pode implementar o algoritmo de ordenação BubbleSort ou usar o método sort ou a função
# sorted para ordenar a lista.

n = int(input("Digite um valor: "))
lista = []

while n != 0:
    lista.append(n)
    n = int(input("Digite um valor: "))

lista.sort()
print(lista)