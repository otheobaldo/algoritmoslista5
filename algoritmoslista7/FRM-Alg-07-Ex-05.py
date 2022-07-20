# 5.

def isAnagrama(palavraA, palavraB):
    conjuntoA = {""}
    conjuntoB = {""}
    for letra in palavraA:
        conjuntoA.add(letra)
    for letra in palavraB:
        conjuntoB.add(letra)
    if conjuntoB == conjuntoA:
        anagrama = True
    else:
        anagrama = False
  
    return(anagrama)

def main():
    t1 = input("Digite a primeira palavra: ")
    t2 = input("Digite a segunda palavra: ")
    x = isAnagrama(t1,t2)
    print(x)

if __name__ == '__main__':
    main()