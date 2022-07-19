# 2. Unidades de tempo (novamente). Neste exercício você deve fazer o processo inverso do
# exercício anterior. Desenvolva um programa Python que recebe do usuário uma quantidade de
# tempo em segundos. Então o programa deve exibir a quantidade de tempo equivalente na
# forma D:HH:MM:SS, onde D, HH, MM e SS representam dias, horas, minutos e segundos
# respectivamente. Os valores de horas, minutos e segundos devem ser formatados todos com
# dois dígitos, sendo obrigatória a inclusão do dígito 0 para valores menores que 10.

segundos = int(input("Digite a quantidade de segundos: "))

minutos = segundos//60 
s = segundos%60 
horas = minutos//60
m = minutos%60
dias = horas//24
h = horas%24

print("Quantida de tempo em D:HH:MM:SS")
print(dias,":","{:02d}".format(h),":","{:02d}".format(m),":","{:02d}".format(s))