# 1. Unidades de tempo. Crie um programa Python que leia do usuário um valor de intervalo de
# tempo expresso em número de dias, horas, minutos e segundos. O programa deve computar e
# exibir a quantidade total de segundos deste intervalo de tempo informado.

dias = int(input("Digite a quantidade de dias: "))
horas = int(input("Digite a quantidade de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))
segundos = int(input("Digite a quantidade de segundos: "))

dias = dias*24*60*60 #dias * horas em um dia * minutos em uma hora * segundos em um minuto
horas = horas*60*60 #horas * minutos em uma hora * segundos em um minuto
minutos = minutos*60 #minutos * segundos em um minuto

t = dias+horas+minutos+segundos
print("A quantidade de tempo em segundos:",t)