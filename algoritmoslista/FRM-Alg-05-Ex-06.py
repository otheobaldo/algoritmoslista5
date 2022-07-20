# 6. Centralizando String

def centralizar(string, largura):
    l = largura//2
    s = " "
    espaço = l * s
    return(espaço+string+espaço)


def main():     
    palavra = input("Insira uma string: ")
    largura = int(input("Insira a largura: "))
    x = centralizar(palavra, largura)
    print(x)

if __name__ == '__main__':
    main()