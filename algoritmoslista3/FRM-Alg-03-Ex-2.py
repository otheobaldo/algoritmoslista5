# 2. Idade canina. É comum dizermos que um ano de um cachorro equivale a 7 anos de um
# humano. Porém, essa conversão simples erra em não reconhecer que cachorros se tornam
# adultos em cerca de 2 anos. Assim, algumas pessoas acreditam que é melhor contar os dois
# primeiros anos como 10.5 anos caninos, e os anos restantes como 4 anos caninos cada.
# Escreva um programa que implemente a conversão de anos cronológicos para anos caninos.
# Certifique-se que seu programa funciona tanto para conversão de idades até 2 anos
# cronológicos e também maiores que 2 anos cronológicos. Seu programa deve exibir uma
# mensagem de erro se o usuário entrar com um número negativo.

idadedog = int(input("Insira a idade do seu cachorro: "))

if idadedog < 0:
    print("Erro: número negativo")
else:
    if idadedog <= 2:
        idade = idadedog*10.5
        print("O seu cachorro tem ",idade," anos caninos")
    else:
        idade = ((idadedog-2)*4)+21
        print("O seu cachorro tem ",idade," anos caninos")