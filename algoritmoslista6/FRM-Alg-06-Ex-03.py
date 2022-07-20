# 3. Removendo extremos. Ao analisar os dados coletados como parte de um experimento
# científico, pode ser desejável remover os valores mais extremos antes de realizar outros
# cálculos. Escreva uma função que tenha uma lista de valores e um número inteiro não
# negativo, n, como seus parâmetros. A função deve criar uma nova cópia da lista com os n
# maiores elementos e os n menores elementos removidos. Em seguida, ele deve retornar a
# nova cópia da lista como o único resultado da função. A ordem dos elementos na lista
# retornada não precisa coincidir com a ordem dos elementos na lista original.
# Escreva um programa principal que demonstre sua função. Sua função main deve ler uma lista
# de números do usuário e remover os dois maiores e os dois menores valores dela. Exiba a
# lista com os extremos removidos, seguido pela lista original. Seu programa deve gerar uma
# mensagem de erro apropriada se o usuário inserir menos de 4 valores.

def listaEx(l, n):
    l.sort()
    del l[:n]
    del l[-n:]

    return(l)

def main():
    valor = input("Digite um valor: ")
    lista = []

    while True:
        if valor == "":
            break
        else:
            lista.append(valor)
            valor = input("Digite um valor: ")

    numero = int(input("Digite o número de elementos à remover: "))
    print(lista)
    l = listaEx(lista, numero)
    print(l)
    print(lista)

    
    


if __name__ == '__main__':
    main()