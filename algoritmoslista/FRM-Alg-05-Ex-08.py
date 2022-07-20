# 08

def letraMaiuscula(frase):
    ultimo = ""
    antepenultimo = ""
    nova_frase = ""
    lpontuacao = ["!", "?", "."]

    for caracter in frase:
        if ultimo == " " and antepenultimo in lpontuacao or ultimo == "":
            c = caracter.upper()
            nova_frase = nova_frase + c
        else:
            nova_frase = nova_frase + caracter
        
        if ultimo in lpontuacao:
            antepenultimo = ultimo
        elif ultimo.isalpha():
            antepenultimo = ""
        ultimo = caracter

    return(nova_frase)

def main():
    txt = input("Digite uma frase: ")
    novo_txt = letraMaiuscula(txt)
    print(novo_txt)

if __name__ == '__main__':
    main()