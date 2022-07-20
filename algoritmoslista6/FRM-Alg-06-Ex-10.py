# 10. Formatando uma lista. Quando escrevemos uma lista em português, geralmente separamos
# os itens por vírgula e colocamos a conjunção “e" entre os dois últimos itens, a não ser que a
# lista só tenha um item. Considere as listas abaixo:

def formatarLista(lista):
    frase = ""
    i = 1

    for item in lista:
        if i == 1:
            frase = item
            i = i + 1
        elif i == len(lista):
            frase = frase + " e " + item         
        else:
            i = i + 1
            frase = frase + ", " + item 
    return frase

def main():
    listaitens = []
    item = input("Digite um item: ")
    while item != "":
        listaitens.append(item)
        item = input("Digite um item: ")             

    frase = formatarLista(listaitens)
    print(frase)
    
if __name__ == '__main__':
    main()