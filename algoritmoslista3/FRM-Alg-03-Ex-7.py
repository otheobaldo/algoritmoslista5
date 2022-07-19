# 7. Níveis de barulho. A tabela abaixo mostra uma lista de volume sonoro em decibéis para
# diferentes tipos comuns de barulhos.

# Escreva um programa Python que receba do usuário um nível de volume em decibéis. Se o
# usuário entrar com um valor igual a um daqueles listados na tabela, então seu programa deve
# exibir uma mensagem informando o tipo de barulho da tabela equivalente ao valor informado.
# Se o usuário entrar um valor intermediário entre dois valores da tabela, então seu programa
# deve exibir uma mensagem informando que o nível está entre os dois barulhos (deve informar
# quais são eles). Certifique-se também que seu programa exiba mensagens apropriadas caso o
# usuário entre com valor menor que o menor valor da tabela ou maior que o maior valor.

dB = int(input("Insira um valor em decibéis (dB): "))

n1 = "Nível 1 - Sala Silenciosa" #40
n2 = "Nível 2 - Despertador" #70
n3 = "Nível 3 - Cortador de grama" #106
n4 = "Nível 4 - Britadeira" #130

if dB < 40: 
    print("O nível de barulho é abaixo do",n1)
elif dB == 40:
    print("O nível de barulho é",n1)
elif dB > 40 and dB <70:
    print("O nível de barulho está entre", n1,"e",n2)    
elif dB == 70:
    print("O nível de barulho é",n2)
elif dB > 70 and dB <106:
    print("O nível de barulho está entre", n2,"e",n3)
elif dB == 106:
    print("O nível de barulho é",n3)
elif dB > 106 and dB <130:
    print("O nível de barulho está entre", n3,"e",n4)
elif dB == 130:
    print("O nível de barulho é",n4)
else:
    print("O nível de barulho é acima do",n4)