# 11. Senha aleatória. Escreva uma função que gere uma senha aleatória. A senha deve ter um
# comprimento aleatório de 7 a 10 caracteres. Cada caractere deve ser selecionado
# aleatoriamente das posições 33 a 126 na tabela ASCII. Sua função não receberá nenhum
# parâmetro. Ele retornará a senha gerada aleatoriamente como seu único resultado. Exiba a
# senha gerada aleatoriamente no programa principal do seu arquivo fonte.

import random

def geraSenha():
    comprimento = random.randint(7,11) 
    x = 0
    senha = ""       
    while x != comprimento:
        caracter = random.randint(33,127)
        caracterl = chr(caracter)
        senha = senha + caracterl 
        x = x + 1
    return senha    

def main():
    print(geraSenha())

if __name__ == '__main__':
    main()
