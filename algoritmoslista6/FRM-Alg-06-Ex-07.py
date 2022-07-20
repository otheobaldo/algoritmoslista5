# 7. Números perfeitos. Um número inteiro positivo n é chamado de número perfeito se a soma
# de todos os divisores de n é igual a n. Por exemplo, 28 é um número perfeito porque seus
# divisores são 1, 2, 4, 7 e 14; e 1+2+4+7+14=28. Escreva uma função para verificar se um
# número é perfeito. A função deve receber somente um número inteiro positivo e retornar True
# se ele for perfeito ou False caso contrário. Escreva uma função main para identificar e imprimir
# todos os números perfeitos de 1 a 10.000. Obs.: você pode usar o código do exercício anterior
# para lhe ajudar nesta tarefa.

def divisaoExata(dividendo):
    ldivisores = []
    n = 0
    while dividendo != n:
        n = n + 1
        if dividendo%n == 0:
            ldivisores.append(n)
        else:
            continue
    del ldivisores[-1]
    return ldivisores

def numeroPerfeito(dividendo, divisores):
    soma = 0
    for divisores in divisores:        
        soma = soma + divisores
    if soma == dividendo:
        x = True
    else:
        x = False
    return x

def main():
    for n in range(1, 10001):
        d = divisaoExata(n)
        perfeito = numeroPerfeito(n, d)
        if perfeito == True:
            print(n)

if __name__ == '__main__':
    main()


