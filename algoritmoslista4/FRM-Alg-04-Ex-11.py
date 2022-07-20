#11. 

x = 0
palavra = input("Insira uma palavra: ")
palavral = palavra.lower()

contpalavra = ""
novapalavra = ""


while x < len(palavral):
    letra = palavral[x]
    x += 1
    if letra != " ":
            novapalavra = novapalavra + letra
            contpalavra = letra + contpalavra
            print(novapalavra)
    else:
        continue

    
print(contpalavra)
if novapalavra == contpalavra:
    print("É palíndromo") 
else:
    print("Não é palíndromo")