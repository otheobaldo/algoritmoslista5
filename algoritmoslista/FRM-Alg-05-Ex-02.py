# 2. Tarifa do táxi. Em uma determinada cidade, as tarifas de táxi consistem em um valor inicial de
# R$ 4,00 mais R$ 0,25 a cada 140 metros percorridos. Escreva uma função que recebe como
# seu único parâmetro a distância percorrida em quilômetros, e retorna como seu único
# resultado o valor total da corrida. Escreva um programa principal que demonstre o
# funcionamento de sua função.


def calcula_valor(distancia):
    d = distancia*1000/140
    v = 4 + (d*0.25)
    return v

def main():
    km = float(input("Distância em km: "))
    x = calcula_valor(km)
    print("O valor total da corrida é R${:.2f}".format(x))

if __name__ == '__main__':
    main()