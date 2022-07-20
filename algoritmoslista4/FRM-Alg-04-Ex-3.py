# 3. Tabela de conversão de temperaturas. Escreva um programa Python que mostre uma tabela
# de conversão de temperaturas em graus Celsius e graus Fahrenheit. A tabela deve incluir em
# suas linhas todas as temperaturas entre 0 e 100 graus Celsius que sejam múltiplas de 10
# graus Celsius. Inclua os cabeçalhos apropriados e tabulações para suas colunas. Pesquise na
# internet sobre a fórmula de conversão de temperaturas Celsius para Fahrenheit

c = 1
i = 0
print ("{:<8} {:<15}".format('Celsius','Fahrenheit'))

while i < 10:
    i = i + 1
    cel = 10 * i
    fah = (cel * 9/5) + 32
    print("{:<8} {:<15}".format(cel,fah))