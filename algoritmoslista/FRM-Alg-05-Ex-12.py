# 12. Verificação de senha válida. Neste exercício, você deve escrever uma função que determina
# se uma senha é válida ou não. Definiremos uma boa senha como aquela que tem pelo menos
# 8 caracteres e contém pelo menos uma letra maiúscula, pelo menos uma letra minúscula e
# pelo menos um número. Sua função deve retornar True se a senha passada a ela como seu
# único parâmetro for válida. Caso contrário, ele deve retornar False. Inclua um programa
# principal que lê a senha do usuário e informa se ela é ou não válida.

def validadorSenha(senha):
    validador = 0
    x1 = 0
    x2 = 0
    x3 = 0

    if len(senha) > 7:
        for caracter in senha:
            o_senha = ord(caracter)
            if o_senha > 64 and o_senha < 91:
                x1 = 1
            elif o_senha > 96 and o_senha < 123:
                x2 = 1
            elif o_senha > 47 and o_senha < 58:
                x3 = 1
            else:
                continue
        validador = x1 + x2 + x3 
        validador = validador == 3

    return validador

def main():
    senha = input("Digite a senha: ")
    x = validadorSenha(senha)
    print(x)

if __name__ == '__main__':
    main()