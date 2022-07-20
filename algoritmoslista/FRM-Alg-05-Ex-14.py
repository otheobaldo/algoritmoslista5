# 14. Datas mágicas. Uma “data mágica” é uma data na qual a multiplicação do dia pelo mês é
# igual aos dois últimos dígitos do ano. Por exemplo, 10 de junho de 1960 é uma data mágica
# porque 10 vezes 6 é igual a 60, que são os dois últimos dígitos do ano. Escreva uma função
# que determina se uma data é ou não mágica. A função deve receber 3 parâmetros inteiros
# (dia, mês e ano), e retornar um valor lógico. Escreva um programa main que utilize sua função
# para determinar e imprimir todas as datas mágicas do século XX. O exercício anterior pode ser
# útil para resolver este problema.

mes31 = [1,3,5,7,8,10,12]
mes30 = [4,6,9,11]

def data_magica(dia, mes, ano):  
    ano = ano - 1900
    if dia * mes == ano:
        return True
    else:
        return False

def main():
    for a in range(1901,2000):
        for m in range(1,13):
            if m in mes31:
                for d in range(1,32):            
                    if (data_magica(d,m,a)) == True:
                        print(d,m,a)
            elif m in mes30:
                for d in range(1,31):            
                    if (data_magica(d,m,a)) == True:
                        print(d,m,a)
            else:
                for d in range(1,29):            
                    if (data_magica(d,m,a)) == True:
                        print(d,m,a)

if __name__ == '__main__':
    main()

            

        
