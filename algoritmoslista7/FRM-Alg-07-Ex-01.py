# 1

def caracteresunicos(tx):
    letrasRep = {""}
    novo_tx = ""
    for letra in tx:
        letrasRep.add(letra)
    if len(letrasRep)-1 == len(tx):
        x = True
    else:
        x = False

    return(x)

def main():
    texto = input("Digite: ")
    x = caracteresunicos(texto)
    print(x)

if __name__ == '__main__':
    main()