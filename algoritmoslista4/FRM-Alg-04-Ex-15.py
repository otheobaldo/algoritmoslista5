# 15. Decimal para binário
binario = ""
decimal = int(input("Insira um decimal inteiro: "))
while decimal != 0:  
    resto = decimal%2
    binario = str(resto) + binario
    decimal = decimal//2
print(binario)