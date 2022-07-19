# 3. Vogal ou consoante. Escreva um programa Python que peça para o usuário uma letra do
# alfabeto. Se o usuário entrar com as letras a, e, i, o ou u, o programa deve exibir uma
# mensagem dizendo que a letra é uma vogal. Caso contrário, o programa deve exibir a
# mensagem informando que a letra é uma consoante.

letra = input("Insira uma letra do alfabeto: ")

if (letra == "a") or (letra == "e") or (letra == "i") or (letra == "o") or (letra == "u"):
    print("É uma vogal")
else:
    print("É uma consoante")
