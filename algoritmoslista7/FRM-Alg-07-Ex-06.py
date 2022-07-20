# 6.

def isAnagrama(palavraA, palavraB):
    
    def conjuntos(palavra):
        conjunto = {""}
        for c in palavra:
            if c.isalpha() == True:                
                conjunto.add(c.upper())
        return(conjunto)
    A = conjuntos(palavraA)
    B = conjuntos(palavraB)    
    if A == B:
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