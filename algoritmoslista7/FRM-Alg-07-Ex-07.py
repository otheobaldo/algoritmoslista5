# 7.
from random import randint

def cartelaBingo():
    def criarLista(x, y):
        conjunto = {0}
        while len(conjunto) != 6:
            valor = randint(x, y)
            conjunto.add(valor)
        conjunto.remove(0)
        lista = list(conjunto)
        lista.sort()            
        return(lista)

    listaB = criarLista(1, 15)
    listaI = criarLista(16, 30)
    listaN = criarLista(31, 45)
    listaG = criarLista(46,60)
    listaO = criarLista(61,75)

    dicionario = {"B":listaB, "I":listaI, "N":listaN, "G":listaG, "O":listaO}   
    return(dicionario)  

def main():
    bingo = cartelaBingo()
    colunas = bingo.values()
    for item in bingo:
        print(item, end="     ")     
    print()
    print("--------------------------")

    i = 0
    for i in range(5):
        for item in colunas:
            print("%02d" %item[i], end="    ")
        i = i + 1
        print()         

if __name__ == '__main__':
    main()