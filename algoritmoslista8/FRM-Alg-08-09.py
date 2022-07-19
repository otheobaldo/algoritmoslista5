from random import randint, random

def raizquadrada(n, estimativa):  
    if abs((estimativa**2)-n) <= 10E-12:
        return(estimativa)
    return(raizquadrada(n,((estimativa+n/estimativa)/2)))

print(raizquadrada(3, estimativa=1))

def main():
    for i in range(10):
        n = randint(1, 100)
        print(n, raizquadrada(n,estimativa=1))

if __name__ == '__main__':
    main()