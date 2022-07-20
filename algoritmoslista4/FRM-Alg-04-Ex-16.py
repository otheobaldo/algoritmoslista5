# 16. Cara ou coroa.
import random

total_sorteios = 0

for simulação in range(10):
    sorteios = 0
    cara = 0
    coroa = 0
    while cara < 3 and coroa <3:
        result = random.randint(0,1)
        if result == 0:
            print("0", end=" ")
            cara = 0
            coroa += 1
        else:
            print("1", end=" ")
            cara += 1
            coroa = 0
        sorteios += 1
    total_sorteios += sorteios
    print("({:d} sorteios)".format(sorteios))
print("Na média, foram necessários {:.1f} sorteios.".format(total_sorteios/10))