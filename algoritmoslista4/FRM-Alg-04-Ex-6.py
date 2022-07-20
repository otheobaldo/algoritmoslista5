# 6. Bits de paridade. Um bit de paridade é um mecanismo para detecção de erros em dados
# transmitidos por uma conexão não confiável, como linha telefônica por exemplo. A idéia básica
# é que, a cada grupo de 8 bits, seja acrescentado um bit adicional de forma que erros em bits
# individuais possam ser detectados.
# Os bit de paridade podem ser computados para paridade par ou paridade ímpar. Se for usada
# paridade par, então o bit de paridade a ser transmitido deve ser tal que o número total de bits
# “1” transmitidos (8 bits de dados + 1 bit de paridade) é par. Se for utilizada paridade ímpar, o
# número total de bits “1” transmitidos deve ser ímpar.
# Escreva um programa Python que compute o bit de paridade para grupos de 8 bits fornecidos
# pelo usuário utilizando paridade par. Seu programa deve ler strings contendo 8 bits (portanto
# as strings vai ser sequencias de 8 caracteres 0 ou 1) até que o usuário entre com uma linha
# em branco. Logo após o usuário fornecer cada string, seu programa deve exibir uma
# mensagem informando se o bit de paridade deve ser 0 ou 1. O programa também deve exibir
# uma mensagem de erro caso o usuário entre com algo que não seja a sequência de 8 bits



while True:
    codigo = input("Insira um grupo de 8 bits: ")
    if not codigo:
        break 
    else:
        if len(codigo) != 8:
            print("Erro")
        else:
            for digito in codigo:
                if int(digito) > 1 or int(digito) < 0:
                    print("Erro")
                    break
                else:
                    continue
            else:       
                contagem = int(codigo.count('1'))
                op = contagem%2
                print("O Bit de paridade é", end=" ")
                if op == 0:
                    print(0)
                else:
                    print(1)
    

