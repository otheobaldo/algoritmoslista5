# 11. Mega-sena. Para ganhar o prêmio da mega-sena, é necessário acertar todos os 6 números
# em seu bilhete com os 6 números entre 1 e 60 sorteados pelo organizador da loteria. Escreva
# um programa que gere uma seleção aleatória de 6 números para um bilhete de mega-sena.
# Certifique-se de que não haja números repetidos entre os sorteados. Exiba os números em
# ordem crescente.
import random
loteria = []

while len(loteria)!= 6:
    numero = random.randint(1,60)    
    loteria.append(numero)
    x = set(loteria)
    loteria = list(x)

loteria.sort()
print(loteria)

