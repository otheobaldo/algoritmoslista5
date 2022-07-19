# 8. Centena, dezena, unidade (novamente). Dado um número de três algarismos N = CDU
# (onde C é o algarismo das centenas, D é o algarismo das dezenas e U o algarismo das
# unidades), considere o número M constituído pelos algarismos de N em ordem inversa, isto é,
# M=UDC. Faça um programa Python para gerar e imprimir M a partir de N (p.ex.:N=123
# ->M=321).

numero = int(input("Insira um número inteiro de 3 digitos: "))

n1 = (numero)//100
centena = n1*100
n2 = (numero-centena)//10
dezena = n2*10
unidade = (numero-centena-dezena)
unidade = unidade*100

soma = unidade+dezena+n1

print("A inversão dos algarismos do número fornecido é",soma)