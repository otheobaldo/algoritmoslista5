# 8. Cifra de César. Um dos primeiros exem..

mensagem = input("Digite a mensagem: ")
deslocamento = int(input("Digite o deslocamento: "))
i = 1
concatenar = " "
   

for letra in mensagem:
    x = (ord(letra))
    x = x + deslocamento
    if x > 122:
        x = x - 26
    elif x > 90 and x < 97:
        x = x - 26            
    y = (chr(x))
    concatenar = concatenar + y

print(concatenar)