# 3. Calculadora de envio e-commerce. Uma loja online fornece envio de seus itens pelo preço
# de R$ 10,95 para o primeiro item e R$ 2,95 para cada um dos demais itens. Escreva uma
# função que receba a quantidade de ítens de um pedido e retorne o valor total do envio de
# acordo com essas regras. Inclua um programa principal que leia do usuário o número de itens
# adquiridos e mostre o custo do envio.

def calcula_frete(qnt_itens):
    valor = 10.95 + (qnt_itens-1)*2.95
    return valor

def main():
    n = int(input("Quantidade de itens: "))
    if n > 1:
        x = calcula_frete(n)
        print("O custo de envio é R$ {:.2f}".format(x))
    else:
        print("ERRO! Digite um número natural maior que 0")

if __name__ == '__main__':
    main()
