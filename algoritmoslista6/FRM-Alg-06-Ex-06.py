# 6. Lista de divisores. Um divisor de um numero inteiro n é um número inteiro positivo menor
# que n, tal que divida n em partes inteiras (divisão exata, sem resto). Escreva uma função
# Python que calcula todos os divisores de um número inteiro positivo. A função deve retornar
# uma lista contendo todos os divisores. Escreva uma função main para demonstrar o
# funcionamento da sua solução, a função main deve ler um número do usuário e imprimir todos
# os seus divisores.

def divisaoExata(dividendo):
    ldivisores = []
    n = 0
    while dividendo != n:
        n = n + 1
        if dividendo%n == 0:
            ldivisores.append(n)
        else:
            continue
    return ldivisores

def main():
    numero = int(input("Digite um número inteiro positivo: "))
    x = divisaoExata(numero)
    print(x)

if __name__ == '__main__':
    main()