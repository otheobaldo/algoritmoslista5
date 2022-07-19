# 9. Data invertida. Admitindo que uma data é lida pelo algoritmo em uma variável inteira, e não
# em uma variável do tipo data, crie um programa Python que leia uma data no formato
# DDMMAA e imprima essa data no formato AAMMDD, onde:
# • a letra D corresponde a dois algarismos representando o dia;
# • a letra M corresponde a dois algarismos representando o mês;
# • a letra A corresponde aos dois últimos algarismos representando o ano.
# Por exemplo: a data 110618 (11 de junho de 2018), deve ser impressa como 180611

data = int(input("Insira a data no formato DDMMAA: "))
dia = data//10000
mes = (data-dia*10000)//100
ano = (data-dia*10000-mes*100)

print("A data no formato AAMMDD: {:02d}".format(ano),"{:02d}".format(mes),"{:02d}".format(dia))