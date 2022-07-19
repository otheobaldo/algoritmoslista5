# 7. Centena, dezena, unidade. Dado um número de três algarismos N = CDU (onde C é o
# algarismo das centenas, D é o algarismo das dezenas e U o algarismo das unidades) Faça um
# programa Python que receba do usuário o número inteiro N, e imprima separadamente a
# centena, a dezena e a unidade.

numero = int(input("Insira um número inteiro de 3 digitos: "))

n1 = numero//100
centena = n1*100
n2 = (numero-centena)//10
dezena = n2*10
unidade = (numero-centena-dezena)

print("A centena é",centena,",a dezena é",dezena,",a unidade é",unidade)