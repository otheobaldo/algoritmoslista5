# 12. A lista está ordenada? Escreva uma função que determina se uma lista de valores está ou
# não em ordem de classificação (crescente ou decrescente). A função deve receber a lista
# como parâmetro e retornar True se a lista já estiver classificada. Caso contrário, ele deve
# retornar False. Escreva um programa principal que leia uma lista de números do usuário e use
# sua função para relatar se a lista é classificada.

def listaOrdenada(lista):

    crescente = sorted(lista)
    decrescente = sorted(lista, reverse=True)
    if lista == crescente or lista == decrescente:
        x= True
    else:
        x= False
    return(x)

def main():
    lista = []
    item = input("Digite um item: ")
    while item != "":    
        lista.append(item)
        item = input("Digite um item: ")
    classificacao = listaOrdenada(lista)
    print(classificacao)

if __name__ == '__main__':
    main()