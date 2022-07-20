# 14. Precedência de operadores. Escreva uma função chamada precedencia que retorna um
# inteiro representando a precedência de um operador matemático. Uma string contendo o
# operador será passada para a função como seu único parâmetro. Sua função deve retornar 1
# para + e -, 2 para * e / e 3 para ^. Se a string passada para a função não for um desses
# operadores, a função deve retornar -1. Inclua um programa principal que lê um operador do
# usuário e exibe a precedência do operador

def precedencia(texto):
    if texto == "+" or texto == "-":
        inteiro = 1
    elif texto == "/" or texto == "*":
        inteiro = 2
    elif texto == "^":
        inteiro = 3
    else:
        inteiro = -1
    return(inteiro)

def main():    
    operador = input("Digite um operador: ")
    x = precedencia(operador)
    if x == -1:
        print("Erro. Não é um operador")
    elif x == 1 or x == 2 or x == 3:
        print("O operador é de precedência", x)

if __name__ == '__main__':
    main()