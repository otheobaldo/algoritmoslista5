# 12. Ano bissexto. A maioria dos anos possui 365 dias. Porém, o tempo para a Terra dar uma volta
# completa em torno do Sol é um pouco maior que isso. Como consequência, um dia extra (29
# de fevereiro) é incluído em alguns anos para compensar essa diferença. Tais anos são
# chamados de anos bissextos. As regras para determinar se um ano é ou não bissexto são as
# seguintes:

ano = int(input("Insira um ano: "))

if (ano%400) == 0:
    print("É ano bissexto")
elif (ano%100) == 0:
    print("Não é ano bissexto")
elif (ano%4) == 0:
    print("É ano bissexto")
else:
    print("Não é bissexto")