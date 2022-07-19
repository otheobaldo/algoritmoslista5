# 1. Par ou ímpar. Escreva um programa Python que recebe do usuário um número inteiro. Seu
# programa deve então exibir uma mensagem indicando se o número fornecido é par ou ímpar.

numero = int(input("Digite um número inteiro: "))

impar_par = numero%2

if numero == 0 :
    print("O número é zero")
else :
    if impar_par == 0 :
        print("O número é par")
    else :
        print("O número é impar")
