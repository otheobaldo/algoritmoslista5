# 10. Cor da casa do tabuleiro. As posições das casas em tabuleiros de xadrez são identificadas
# por uma letra e um número. A letra identifica a coluna e o número define a linha, conforme a
# figura abaixo:

posicao = input("Insira a posição da casa do tabuleiro: ")

l = int(posicao[1])%2

if (posicao[0] == "b") or (posicao[0] == "d") or (posicao[0] == "f") or (posicao[0] == "h"):
    c = 0
else:
    c = 1

if (l == 0) and (c == 0):
    print("A casa",posicao,"é preta")
elif (l == 1) and (c ==1):
    print("A casa",posicao,"é preta")
else:
    print("A casa",posicao,"é branca")
