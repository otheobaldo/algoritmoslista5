# 4. Mediana de três valores. Escreva uma função que recebe três números como parâmetros e
# retorna o valor da mediana desses parâmetros como seu resultado. Inclua um programa
# principal que lê três valores do usuário e exibe a mediana destes valores.

def calcula_mediana(n1, n2, n3):
    if (n1 > n2 and n2 > n3) or (n3 > n2 and n2 > n1):
        x = n2
    elif (n2 > n3 and n3 > n1) or (n1 > n3 and n3 > n2):
        x = n3  
    else:
        x = n1
    return x

def main():     
    num1 = int(input("Digite o 1° número: "))
    num2 = int(input("Digite o 2° número: "))      
    num3 = int(input("Digite o 3° número: "))
    x = calcula_mediana(num1,num2,num3)
    print("A mediana é", x)

if __name__ == '__main__':
    main()