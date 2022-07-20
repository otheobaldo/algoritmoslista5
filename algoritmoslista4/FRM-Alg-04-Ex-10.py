# 10. Palindromo

x = 0
palavra = input("Insira uma palavra: ")
contpalavra = ""

while x < len(palavra):
    letra = palavra[x]
    contpalavra = letra + contpalavra
    x +=1
if palavra == contpalavra:
    print("É palíndromo") 
else:
    print("Não é palíndromo")   
