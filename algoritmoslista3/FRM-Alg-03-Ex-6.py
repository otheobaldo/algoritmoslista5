# 6. Classifique o triângulo. Baseado nos comprimentos dos seus lados, um triângulo pode ser
# classificado como equilátero (quando os três lados tem o mesmo tamanho), isósceles (quando
# apenas dois lados são iguais) ou escaleno (quando os três lados são diferentes). Escreva um
# programa Python que recebe do usuário os comprimentos dos 3 lados de um triângulo e exiba
# uma mensagem informando qual é o tipo do triângulo.

l1 = float(input("Insira o valor dos lados do triângulo: "))
l2 = float(input("Insira o valor dos lados do triângulo: "))
l3 = float(input("Insira o valor dos lados do triângulo: "))

if l1 == l2 == l3:
    print("O triângulo é equilátero")
elif (l1 == l2) or (l2 == l3) or (l1 == l3):
    print("O triângulo é isóceles")
else:
    print("O triângulo é escaleno")