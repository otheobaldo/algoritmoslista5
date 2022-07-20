# 7. Aproximação do valor de pi. O valor aproximado de pode ser calculado pela série infinita
# apresentada abaixo:

# Escreva um programa Python que exiba 15 aproximações de . A primeira aproximação deve
# ter apenas o primeiro termo da série (ou seja, o valor resultante vai ser somente 3). Cada nova
# aproximação de mostrada pelo seu programa deve incluir mais um termo da série, sendo
# cada vez uma aproximação mais precisa do que a anterior.
i = 1
n1 = 0
n2 = 1
n3 = 2
n = 0
oldn = 0

while i <=15:
    i = i + 1
    n1 = n1 + 2
    n2 = n2 + 2
    n3 = n3 + 2
    n =4/((n1)*(n2)*(n3))  
    if i%2 == 0: 
        oldn = oldn + n
        soma = 3 + oldn + n
    else:
        oldn = oldn - n
        soma = 3 + oldn - n  
    print(soma)   
print("fim")