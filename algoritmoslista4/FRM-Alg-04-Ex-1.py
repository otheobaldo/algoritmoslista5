# 1. Média aritmética. Escreva um programa Python que calcula a média aritmética de um
# conjunto de valores fornecidos pelo usuário. O usuário deve entrar com o valor 0 indicando
# que não serão mais fornecidos novos valores. Seu programa deve exibir uma mensagem de
# erro se o primeiro valor fornecido pelo usuário for 0.

x = float(input("Digite uma nota: "))
i = 0
soma = 0
if x != 0:
    while x != 0:
        soma = soma + x
        i += 1
        x = float(input("Digite uma nota: "))
    else:
        media = soma/i
        print("A média é ", media)
else:
    print("ERRO")