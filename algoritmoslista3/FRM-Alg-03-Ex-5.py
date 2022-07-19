# 5. Nome do mês e número de dias. A quantidade de dias de um mês pode variar de 28 a 31
# dias. Neste exercício você deve criar um programa Python que recebe do usuário o nome de
# um mês (como uma string). Então seu programa deve exibir uma mensagem informando a
# quantidade de dias daquele mês. Caso o mês seja fevereiro, sua mensagem pode informar
# “28 ou 29 dias”.

mes = input("Insira um mês: ").lower()

if (mes == "janeiro") or (mes == "março") or (mes == "maio") or (mes == "julho") or (mes == "agosto") or (mes == "outubro") or (mes == "dezembro"):
    print("31 dias")
elif (mes == "fevereiro"):
    print("28 ou 29 dias")
elif (mes == "abril") or (mes == "junho") or (mes == "setembro") or (mes == "novembro"):
    print("30 dias")
else:
    print("Inválido")
