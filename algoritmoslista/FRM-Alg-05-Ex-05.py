# 5. Números ordinais. Palavras como primeiro, segundo e terceiro são chamadas de números
# ordinais. Neste exercício, você deve escrever uma função que recebe um inteiro como seu
# único parâmetro e retorna uma string contendo o número ordinal em português como seu
# único resultado. Sua função deve lidar com números inteiros entre 1 e 12 (inclusive). Ela deve
# retornar uma string vazia se um valor fora desse intervalo for fornecido como um parâmetro.
# Inclua um programa principal que demonstra sua função exibindo cada inteiro de 1 a 12 e seu
# respectivo número ordinal.

def extenso(numero):
    if numero >= 1 and numero <= 12:
        if numero == 1:
            x = "Primeiro"
        elif numero == 2:
            x = "Segundo"
        elif numero == 3:
            x = "Terceiro"
        elif numero == 4:
            x = "Quarto"
        elif numero == 5:
            x = "Quinto"
        elif numero == 6:
            x = "Sexto"
        elif numero == 7:
            x = "Sétimo"
        elif numero == 8:
            x = "Oitavo"
        elif numero == 9:
            x = "Nono"
        elif numero == 10:
            x = "Décimo"
        elif numero == 11:
            x = "Décimo Primeiro" 
        else:
            x = "Décimo Segundo" 
    else:
        print("Erro")        
    return x
    
def main():     
    n = int(input("Insira um número (de 1 a 12): "))
    x = extenso(n)
    print(x)

if __name__ == '__main__':
    main()