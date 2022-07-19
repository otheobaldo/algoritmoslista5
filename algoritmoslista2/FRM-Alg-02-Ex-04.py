#4. Ordenação de 3 inteiros. Crie um programa que obtém 3 números inteiros do usuário e os
# exibe de forma ordenada do menor para o maior. Use as funções min e max para encontrar o
# menor valor e o maior valor. Dica: o valor do meio pode ser obtido pela soma dos três valores,
# subtraída do maior e do menor.

n1 = int(input("Insira o primeiro número inteiro: "))
n2 = int(input("Insira o segundo número inteiro: "))
n3 = int(input("Insira o terceiro número inteiro: "))


n_max = max(n1,n2,n3)
n_min = min(n1,n2,n3)
n_meio = (n1+n2+n3)-n_max-n_min

print("Forma ordenada do menor para o maior: ")
print(n_min,n_meio,n_max)