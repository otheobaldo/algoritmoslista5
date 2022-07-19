# 11. Raízes de equação quadrática. Uma função quadrática pode ser descrita da seguinte forma:
# , onde a, b e c são constantes, e a é diferente de zero. As raízes da
# função quadrática podem ser encontradas determinando-se os valores de x que satisfaçam a
# equação quadrática . Uma função quadrática pode ter 0, 1 ou 2 raízes
# reais. Essas raízes podem ser calculadas pela fórmula da Bháskara, mostrada abaixo:

a = int(input("Insira o valor de a: "))
b = int(input("Insira o valor de b: "))
c = int(input("Insira o valor de c: "))

delta = b**2 - 4*a*c

raiz1 = (-b + delta**(1/2))/2*a
raiz2 = (-b - delta**(1/2))/2*a

if (delta == 0):
    print("A expressão possui uma raiz")
    print(raiz1)
elif (delta > 0):
    print("A expressão possui duas raizes")
    print(raiz1,raiz2)
else:
    print("A equação não possui raizes reais")
