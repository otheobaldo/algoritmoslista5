# 10. Números primos. Um número inteiro positivo é primo se e somente se ele for divisível apenas
# por 1 e por ele mesmo. Escreva uma função que recebe um valor inteiro positivo e retorna
# True se ele for primo ou False se ele não for. Escreva um programa principal que leia um
# número inteiro do usuário e exiba uma mensagem indicando se ele é ou não primo.

def primo(num):
    i = 0
    n = 
    for num in range(2, int(n**0.5)+1):
        x = num%n
        if x == 0:
            count += 1
        else:
            count = 0  
    if count > 0:
        logica = "False"
    else:
        logica = "True"   
    return logica

def main():
    numero = input("Digite: ")
    x = primo(numero)
    print(x)

if __name__  == '__main__':
    main()