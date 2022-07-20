# 13. Contagem de elementos. A biblioteca padrão de funções do Python possui um método
# chamado count, que determina quantas vezes um determinado valor ocorre em uma lista.
# Neste exercício você deve criar uma nova função chamada countRange que deve determinar
# e retornar a quantidade de elementos em uma lista que são maiores ou iguais a um valor
# mínimo e menores que um valor máximo. Sua função deve receber três parâmetros: a lista (de
# números), o valor mínimo e o valor máximo. Ela deve retornar um valor inteiro maior ou igual a
# zero. Escreva uma função main demonstrando o funcionamento de sua função.
from itertools import count

def countRange(lista, max, min):
    contagem = 0
    for n in lista:
        if n >= min and n < max:
            contagem = contagem + 1
    return(contagem)

def main():
    listaCount = []
    valor = input("Digite um valor: ")
    while valor != "":
        listaCount.append(int(valor))
        valor = input("Digite um valor: ")
    valorMin = int(input("Digite o valor mínimo: "))
    valorMax = int(input("Digite o valor máximo: ")) 
    x = countRange(listaCount, valorMax, valorMin)
    print(x)

if __name__ == '__main__':
    main()