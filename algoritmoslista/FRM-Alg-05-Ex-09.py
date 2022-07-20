# ; Letras maiúsculas. Muitas pessoas não usam letras maiúsculas corretamente, especialmente
# ; ao digitar em smartphones. Neste exercício, você escreverá uma função que coloca em
# ; maiúscula os caracteres apropriados em uma string. O primeiro caractere da string deve ser
# ; convertido em letra maiúscula, assim como o primeiro caractere (que não seja espaço) após
# ; um “.”, “!” ou "?". Por exemplo, se a função for fornecida com a string “que horas eu tenho que
# ; estar lá? qual é o endereço?" então ele deve retornar a string “Que horas eu tenho que estar
# ; lá? Qual é o endereço?". Inclua um programa principal que leia uma string do usuário, corrige
# ; as letras maiúsculas usando sua função e exibe o resultado.

def corrigirFrase(frase):
    i = 0 
    concatenar = ""
    y = ""

    frase = frase.capitalize()

    for caracter in frase:            
        if caracter == "." or caracter == "?" or caracter =="!":
            y = frase[i+2].upper()
            i = i + 1
            concatenar = concatenar + caracter + " " +  y
        else:
            if caracter == 
            i = i + 1
            concatenar = concatenar + caracter
    
    return concatenar

def main():
    frase = input("Digite a frase: ")
    x = corrigirFrase(frase)
    print(x)

if __name__ == '__main__':
    main()