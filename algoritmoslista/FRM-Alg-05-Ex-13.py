# 13 Dias em um mês. Escreva uma função que determina quantos dias há em um determinado
# mês. Sua função deve receber dois parâmetros: o mês como um número inteiro entre 1 e 12 e
# o ano como um número inteiro de quatro dígitos. Certifique-se de que sua função retorne o
# número correto de dias em fevereiro para os anos bissextos. Inclua um programa principal que
# lê um mês e ano do usuário e exibe o número de dias naquele mês. O exercício 12 da lista 3
# pode ajudá-lo a resolver esse problema.

def ano_bissexto(ano):
    if (ano%400) == 0:
        x = 1
    elif (ano%100) == 0:
        x = 0
    elif (ano%4) == 0:
        x = 1
    else:
        x = 0
    return x

def qnt_dias(mes,ano):
    m31 = [1,3,5,7,8,10,12]
    m30 = [4,6,9,11]
    if mes in m31:
        resposta = "Tem 31 dias"
    elif mes in m30:
        resposta = "Tem 30 dias"
    else:
        if ano_bissexto(ano) == 1:
            resposta = "Tem 29 dias"
        else:
            resposta = "Tem 28 dias"    
    return resposta        

def main():
    ano = int(input("Ano: "))
    mes = int(input("Mês: "))
    print(qnt_dias(mes,ano))

if __name__ == '__main__':
    main()
