# 3.

def buscaReversa(dicio, chave):
    listaValores = []
    for verbete in dicio:
        if verbete == chave:
            listaValores.append(dicio[verbete])    
    return(listaValores)

def main():
    d = {1:"a", 2:"b",3:"C",4:"d"}
    k = int(input("Digite a chave: "))
    x = buscaReversa(d, k)
    print(x)

if __name__ == '__main__':
    main()