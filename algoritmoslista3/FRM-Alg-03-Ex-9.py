# 9. Data de feriado. A tabela abaixo mostra os feriados nacionais brasileiros que caem sempre no
# mesmo dia (em oposição aos feriados variáveis como carnaval e corpus christi).

# Escreva um programa Python que leia do usuário o mês e o dia de uma determinada data. Se
# o mês e o dia corresponderem a uma das datas da tabela acima, seu programa deve exibir o
# nome do feriado. Caso contrário o programa deve informar que o dia e o mês informados não
# correspondem a um feriado nacional.
# Confraternização universal 1o. de janeiro
# Tiradentes 21 de abril
# Dia do trabalho 1o. de maio
# Independência do Brasil 7 de setembro
# Nossa Senhora Aparecida 12 de outubro
# Finados 2 de novembro
# Proclamação da República 15 de novembro
# Natal 25 de dezembro

dia = int(input("Insira o dia: "))
mes = int(input("Insira o mês: "))


if (dia == 1) and (mes == 1):
    print("Hoje é Confraternização Universal")
elif(dia == 1) and (mes == 5):
    print("Hoje é Dia do Trabalho")
elif(dia == 21) and (mes == 4):
    print("Hoje é Tiradentes")
elif(dia == 7) and (mes == 9):
    print("Hoje é feriado da Idependência do Brasil")
elif(dia == 12) and (mes == 10):
    print("Hoje é Dia da Nossa Senhora Aparecida")
elif(dia == 2) and (mes == 11):
    print("Hoje é feriado de Finados")
elif(dia == 15) and (mes == 11):
    print("Hoje é feriado da Proclamação da República")
elif(dia == 25) and (mes == 12):
    print("Hoje é feriado do Natal")
else:
    print("Hoje não é feriado nacional")