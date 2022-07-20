# 5. Valor das entradas. Um determinado zoológico estipula o valor da entrada baseado na idade
# do visitante. Visitantes com até dois anos de idade não precisam pagar. Crianças entre 3 e 12
# anos de idade pagam R$ 14.00. Idosos com 65 anos ou mais pagam R$ 18.00. Todos os
# demais pagam R$ 23.00. Crie um programa que inicia lendo as idades, uma por uma, de um
# grupo de pessoas. O usuário deve entrar uma linha em branco para indicar que não há mais
# pessoas no grupo. Depois disso, seu programa deve exibir uma mensagem informando o
# preço total de todas as entradas para o grupo. O valor deve ser exibido com duas casas
# decimais.

# 14 #Crianças entre 3 e 12 anos
# 18 #Idosos com mais de 65 anos
# 23 #Demais

soma = 0

while True:
    idade = input("Idade: ")
    if not idade:
        break
    else:
        idade = int(idade)
        if (idade >= 3) and (idade <= 12):
            valor = 14
        elif (idade >= 65):
            valor = 18
        elif (idade < 3):
            valor = 0
        else:
            valor = 23
        soma = valor + soma
print("O valor total: ", soma)
