#9.
from random import randint
import random

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

def colunavence(bingo):
    
        somaColuna = 0  
        for chaves in bingo:
            somaColuna = sum(bingo[chaves])
            if somaColuna == 0:
                return True
            else:
                continue

def linhavence(bingo):
    valores = bingo.values()
    somaLinha = 0
    for i in range(5):
        for l in valores:
            somaLinha = somaLinha + l[i]    
        if somaLinha == 0:
            return True
        else:
            somaLinha = 0
        
def diagonalvence(bingo):
    valores = bingo.values()
    somadiagonal = 0
    contador = 0
    for lista in valores:
        contador = contador + 1
        contador2 = 0
        for item in lista:
            contador2 = contador2 + 1
            if contador == contador2:
                somadiagonal = somadiagonal + item
                
    somadiagonalop = 0
    contador3 = 0
    for lista in valores:
        contador3 = contador3 + 1
        contador4 = 0
        for item in lista:
            contador4 = contador4 + 1
            if contador3 + contador4 == 6:
                somadiagonalop = somadiagonalop + item

    if somadiagonalop == 0 or somadiagonal == 0:
        return True

def simulaBingo():
    bingo = cartelaBingo()
    chamadasBingo = ["B1","B2","B3","B4","B5","B6","B7","B8","B9","B10","B11","B12","B13","B14","B15","I16","I17","I18","I19","I20","I21","I22","I23","I24","I25","I26","I27","I28","I29","I30","N31","N32","N33","N34","N35","N36","N37","N38","N39","N40","N41","N42","N43","N44","N45","G46","G47","G48","G49","G50","G51","G52","G53","G54","G55","G56","G57","G58","G59","G60","O61","O62","O63","O64","O65","O66","O67","O68","O69","O70","O71","O72","O73","O74","O75"]
    random.shuffle(chamadasBingo)
    chamadas = 0

    for sorteado in chamadasBingo:
        chamadas = chamadas + 1
        chave = sorteado[0]
        valor = int(sorteado[1:3])
        if valor in bingo[chave]:
            i = 0
            while i < len(bingo[chave]):  
                if bingo[chave][i] == valor:
                    bingo[chave][i] = 0
                i += 1
        if colunavence(bingo) == True or linhavence(bingo) == True or diagonalvence(bingo)== True:
            break
    
    return(chamadas)

def main():
    todaschamadas = []
    somachamadas = 0
    for n in range(1000):        
        quntchamadas = simulaBingo()
        somachamadas = somachamadas + quntchamadas
        todaschamadas.append(quntchamadas)
        n += 1 

    print("Mínimo: %.0f"%min(todaschamadas))
    print("Média: %.0f"%(somachamadas/1000))
    print("Máximo: %.0f"%max(todaschamadas))

if __name__ == '__main__':
    main()