# 2

def inteConjuntos(A, B):
    C = A.difference(B)
    D = B.difference(A)
    E = C.union(D)
    E = list(E)
    E.sort() 
    return(E)

def main():
    m = {2, 4, 5, 9}
    n = {2, 4, 11, 12}
    x = inteConjuntos(m, n)
    print(x)

if __name__ == '__main__':
    main()