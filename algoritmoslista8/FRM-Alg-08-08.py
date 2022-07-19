# 8. 
def dectobinrec(a):  
    if a <= 1:
        return(a)
    r = a%2    
    binario = str(dectobinrec(a//2)) + str(r)
    return(binario)

def main():
    n = int(input("Digite um número inteiro positivo: "))
    if n < 0:
        print("Erro! O número deve ser positivo")
    print(dectobinrec(n))

if __name__ == '__main__':
    main()