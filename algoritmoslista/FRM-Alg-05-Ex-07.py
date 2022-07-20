#07

def criarTriangulo(a,b,c):
    if (a >= b + c) or (b >= c + a) or (c >= b + a):
        return("Triângulo inválido")
    else:
        return("Triâgunlo válido")

def main():    
    l1 = int(input("Digite o valor do lado 1: "))
    l2 = int(input("Digite o valor do lado 2: "))
    l3 = int(input("Digite o valor do lado 3: "))
    print(criarTriangulo(l1,l2,l3))

if __name__ == '__main__':
    main()