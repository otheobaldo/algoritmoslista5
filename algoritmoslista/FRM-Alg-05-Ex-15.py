# 15. Dígitos hexadecimais e decimais. Escreva duas funções chamadas hex2int e int2hex,
# que devem fazer a conversão entre dígitos hexadecimais (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D,
# E e F) e números inteiros de base 10 . A função hex2int é responsável por converter uma
# string contendo um único dígito hexadecimal em um inteiro de base 10, enquanto a função
# int2hex é responsável por converter um inteiro entre 0 e 15 em um único dígito hexadecimal.
# Cada função pegará o valor a ser convertido como seu único parâmetro e retornará o valor
# convertido como o único resultado da função. Certifique-se de que a função hex2int funcione
# corretamente para letras maiúsculas e minúsculas. Observação: se você não sabe como
# converter números entre bases diferentes, veja o quadro explicativo ao final da lista de
# exercícios.

x = int(input("Digite: "))

def int2hex(numero):
    i = -1
    while numero != 1:
        numero = numero/10
        i = i + 1
    lhex = ["A","B","C","D","E","F"]
    if i > 9:
        i = i - 10
        i = lhex[i]       
    return i

def hex2int(numero):
    lhex = ["A","B","C","D","E","F"]
    if numero in lhex:
        for i in lhex:
            numero = i

    i = numero
    while i != 1:
        numero = numero*10
        i = i - 1
    
    if i > 9:
        i = i - 10
        i = lhex[i]       
    return i    

print(hex2int(x))