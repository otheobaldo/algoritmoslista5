# 9. Abaixo e acima da média. Escreva um programa que leia números do usuário até que uma
# linha em branco seja inserida. Seu programa deve exibir a média de todos os valores inseridos
# pelo usuário. Em seguida, o programa deve exibir todos os valores abaixo da média, seguidos
# por todos os valores médios (se houver), seguidos por todos os valores acima da média. Uma
# mensagem apropriada deve ser exibida antes de cada lista de valores.
def media(lvalores):
    maiorMedia = []
    menorMedia = []
    igualMedia = []
    i = 1
    soma = 0

    for valores in lvalores:
        soma = soma + valores
        i = i + 1
    media = soma/i

    for valores in lvalores:
        if valores > media:
            maiorMedia.append(valores)
        elif valores < media:
            menorMedia.append(valores)
        else:
            igualMedia.append(valores)
    return (media, maiorMedia, menorMedia, igualMedia)

def main():
    lvalores = []
    valor = input("Digite um valor: ")
    while valor != "":
        lvalores.append(int(valor))
        valor = input("Digite um valor: ")        

    valormedio, listamaior, listamenor, listaigual = media(lvalores)
    print("O valor médio é ", valormedio)
    print("Os valores abaixo da média é/são ", listamenor)
    print("Os valores acima da média é/são ", listamaior)
    print("Os valores iguais a média é/são ", listaigual)

if __name__ == '__main__':
    main()