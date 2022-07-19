#6. Soma dos dígitos de um inteiro. Desenvolva um programa que obtenha do usuário um
#número inteiro de 4 dígitos e exiba a soma dos dígitos do número. Por exemplo, se o usuário
#fornecer o número 3141, então seu programa deve exibir o número 9 (3 + 1 + 4 + 1).

numero = int(input("Insira um número inteiro de 4 digitos: "))

n1 = numero//1000
mil = n1*1000
n2 = (numero-mil)//100
cem = n2*100
n3 = (numero-mil-cem)//10
dez = n3*10
n4 = (numero-mil-cem-dez)

soma = n1+n2+n3+n4

print("A soma dos algarismos do número inteiro fornecido é",soma)