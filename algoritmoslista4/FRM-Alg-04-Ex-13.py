# 13. Fatoração numérica
# Inicialize fator com valor 2
# Enquanto fator for menor ou igual a n, faça
# Se n for divisível por fator então
# Concluímos que fator faz parte da fatoração de n
# Faça divisão inteira de n por fator
# Senão
# Incremente fator em uma unidade

n = int(input("Digite um número inteiro (maior ou igual a 2): "))
fator = 2

while fator <= n: 
    if (n%fator == 0):
        print(fator)
        n = n/fator
    else:
        fator += 1
