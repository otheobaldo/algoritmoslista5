# 2. Tabela de descontos. Uma loja está oferecendo uma liquidação com descontos de 60% em
# uma variedade de produtos em final de estoque. O vendedor gostaria de ajudar seus clientes a
# determinar o preço reduzido (com desconto) de seus produtos. Ele quer criar uma tabela que
# mostra os preços originais e os preços após o desconto ser aplicado. Escreva um programa
# Python usando laço de repetição que gere esta tabela mostrando o preço original, o valor de
# desconto e o novo valor com desconto aplicado para produtos com os seguintes valores:
# R$ 4.95, R$ 9.95, R$ 14.95, R$ 19.95 e R$ 24.95. Certifique-se que todos os valores são
# mostrados com duas casas decimais.

i = 4.95
n = 1

print ("{:<8} {:<15} {:<22}".format('Valor','Desconto', "Valor com desconto"))

while n <= 5:    
    j = i*0.6
    k = i*0.4
    print("{:<8} {:<15} {:<22}".format(i,"%.2f"%j,"%.2f"%k))
    i = i+5      
    n += 1 