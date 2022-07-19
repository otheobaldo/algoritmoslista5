# 7. 
def dectobinint(a):  
    binario = ""
    while a != 0:
        r = a%2
        binario = str(r) + binario
        a = a//2
    return(binario)

print(dectobinint(9))