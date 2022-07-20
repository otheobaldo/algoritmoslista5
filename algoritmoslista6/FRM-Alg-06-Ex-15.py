# Um sinal de + ou de - é um operador se o caractere (diferente de espaço em branco)
# imediatamente anterior fizer parte de um número ou se o caractere (diferente de espaço em
# branco) imediatamente antes for um parêntese fechado. Caso contrário, faz parte de um
# número.
# Escreva uma função que pegue uma string contendo uma expressão matemática como seu
# único parâmetro e a divida em uma lista de tokens. Cada token deve ser um parêntese, um
# operador ou um número com um sinal opcional de + ou - (para simplificar, trabalharemos
# apenas com inteiros neste problema). Retorne a lista de tokens como o resultado da função.

operacao = input("Digite uma operação: ")

novaOperacao = ""
tolkens = []
for caracter in operacao:
    if caracter == " ":
        caracter = ""
    novaOperacao = novaOperacao + caracter

print(novaOperacao)
ln = ["1","2","3","4","5","6","7","8","9","0"]
antcaracter = ""

for caracter in novaOperacao:    
    
    if caracter == "+" or caracter == "-":
        if antcaracter == ")" or antcaracter in ln:
            continue
        else:
            o = True
    
    tolkens.append(caracter) 
    antcaracter = caracter

print(tolkens)