#5. Calculando o troco. Considere o software que controla uma máquina automática de compras. 
# Uma tarefa que ele precisa realizar é determinar quanto troco fornecer ao comprador quando
# este faz o pagamento em dinheiro. Escreva um programa Python que inicia lendo do usuario
# uma quantidade de centavos como um número inteiro (portanto vamos considerar números de
# 0 a 99). Então o seu programa deve calcular e exibir quantidade e o valor de cada moeda para
# compor este troco em centavos informado. O troco deve ser montado com a menor quantidade
# possível de moedas. Assuma que a máquina possui moedas de 50, 25, 10, 5 e 1 centavos.

centavos = int(input("Insira a quantidade de centavos (De 0 a 99): "))

q_50 = centavos//50
r_50 = centavos%50

q_25 = r_50//25
r_25 = r_50%25

q_10 = r_25//10
r_10 = r_25%10

q_5 = r_10//5
r_5 = r_10%5

q_1 = r_5

print("Quantidade de moedas para troco:")
print("50 centavos: ",q_50)
print("25 centavos: ",q_25)
print("10 centavos: ",q_10)
print("5 centavos: ",q_5)
print("1 centavo: ",q_1)