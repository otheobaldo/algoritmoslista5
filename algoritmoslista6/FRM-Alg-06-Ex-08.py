# 8. Somente palavras. Neste exercício você deve criar uma função em Python que recebe um
# texto em uma string e retorna uma lista somente com as palavras, sem espaços ou símbolos
# de pontuação. Por exemplo, se a string for: “Beleza! Este é um ótimo exemplo, você
# não acha?”, sua função deveria retornar a seguinte lista: [ “Beleza", “Este", “é",
# “um", “ótimo", "exemplo", “você", “não", “acha”]. Escreva uma função main
# que demonstre o funcionamento da sua solução.

from re import L


def soPalavras(frase):
    l1 = [".", ",", "!", "?", ":", ";", "(", ")", "-", "_"]
    nfrase = ""
    for caracter in frase:
        if caracter in l1:
            caracter = ""
        nfrase = nfrase + caracter
    lpalavras = nfrase.split(" ")
    return lpalavras


def main():
    texto = input("Digite o texto: ")
    novo_texto = soPalavras(texto)
    print(novo_texto)

if __name__ == '__main__':
    main()


