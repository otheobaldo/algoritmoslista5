# 2. Ordem decrescente. Escreva um programa Python que leia números inteiros (do usuário) e
# os armazena em uma lista. Seu programa deve continuar lendo inteiros até que o usuário
# entre com o valor 0 (zero). Então, o programa deve exibir em ordem decrescente todos os
# números digitados pelo usuário sem incluir o valor 0, com um valor em cada linha impressa.

n = int(input("Digite um valor: "))
lista = []

while n != 0:
    lista.append(n)
    n = int(input("Digite um valor: "))

lista.sort(reverse=True)
print(lista)