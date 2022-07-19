# 4. Polígono regular. Crie um programa Python que determina e exibe o nome de um polígono
# regular sendo fornecida pelo usuário a quantidade de lados. Seu programa deve suportar
# polígonos de 3 a 10 lados (inclusive). Caso o usuário forneça valores fora desta faixa, o
# programa deve exibir uma mensagem de erro.

lados = int(input("Insira a quantida de lados do polígono: "))

if lados > 10:
    print("Erro: Maior que 10")
elif lados < 3 :
    print("Erro: Menor que 3 lados")
elif lados == 3:
    print("Triângulo")
elif lados == 4:
    print("Retângulo")    
elif lados == 5:
    print("Pentágono") 
elif lados == 6:
    print("Hexágono")
elif lados == 7:
    print("Heptágono")
elif lados == 8:
    print("Octógono")
elif lados == 9:
    print("Eneágono")
else:
    print("Decágono")