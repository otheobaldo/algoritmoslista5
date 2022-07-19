#10
def descompactar(lista):
    listaDescompactada = [lista[0]] * int(lista[1])
    if len(lista) == 2:
        return (listaDescompactada)
    return(listaDescompactada + descompactar(lista[2:]))

def main():
    lista = ["A", 12, "B", 4, "A", 6, "B", 6]
    print(descompactar(lista))

if __name__ == '__main__':
    main()