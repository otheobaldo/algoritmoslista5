# 4. Evitando duplicatas. Crie um programa Python que leia palavras do teclado até que o
# usuário forneça uma palavra vazia (somente a tecla enter). Depois disso, seu programa deve
# mostrar somente uma vez cada palavra digitada pelo usuário. Ou seja, se o usuário forneceu
# mais de uma vez a mesma palavra, ela só poderá ser exibida uma vez. As palavras devem ser
# exibidas na mesma ordem em que foram digitadas. Por exemplo, se o usuário digitar:

def eliminarDuplicata(lista):
    x = set(lista)
    nova_lista = list(x)
    return nova_lista

def main():
    l_palavras = []

    palavra = input("Digite uma palavra: ")
    while palavra != "":
        l_palavras.append(palavra)
        palavra = input("Digite uma palavra: ")
    print(eliminarDuplicata(l_palavras))
    
if __name__ == '__main__':
    main()