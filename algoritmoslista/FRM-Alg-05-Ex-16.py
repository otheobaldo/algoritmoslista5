# Conversão arbitrária de base numérica. Escreva um programa que permita ao usuário
# converter um número de uma base para base 10 e vice-versa. Seu programa deve suportar
# bases entre 2 (binário) e 16 (hexadecimal) para o número de entrada e o número de resultado.
# Divida seu programa em várias funções, incluindo uma função que converte de uma base
# arbitrária em uma base 10, uma função que converte de uma base 10 em uma base arbitrária.
# A primeira função deve receber como parâmetros uma string com o número a ser convertido
# para base 10, e o valor da base deste número (portanto, de 2 a 16) e deve retornar como
# resultado o número convertido na base 10. A segunda função deve receber como parâmetros
# um numero na base 10 e a base para qual queremos converter o número. Como resultado, a
# função deve retornar uma string com o número convertido. Além disso, faça um programa
# principal que lê as bases e o número de entrada do usuário. Você pode encontrar parte da
# solução deste problema no exercício anterior e nos exercícios 14 e 15 da lista 4.

def binario2decimal(numero):
    c_virgula = 0
    n_numero= ""

    for n in numero:
        if n == ",":
            expoente = c_virgula - 1
        else:
            c_virgula = c_virgula + 1
            n_numero = n_numero + n              

    i = 0
    decimal = 0

    for n in n_numero:
        n = int(n)
        n = n*2**(expoente-i)
        i = i + 1
        decimal = n + decimal

    return decimal

def hexa2decimal(numero):
    i = 0
    decimal = 0

    for n in numero:
        if ord(n) > 64 and ord(n) < 91:
            n = ord(n) - 55
        elif ord(n) > 96 and ord(n) < 123:
            n = ord(n) - 87
        else:
            n = int(n)
        expoente = int(len(numero)-1)
        conversao = n*16**(expoente-i)
        decimal = conversao + decimal
        i = i + 1
        
    return decimal

def main():
    numero = input("Digite o número a ser convertido: ")
    base = int(input("Digite a base (2 ou 16): "))
    if base == 2:
        x = binario2decimal(numero)
    else:
        x = hexa2decimal(numero)    
    print(x)

if __name__  == '__main__':
    main()
