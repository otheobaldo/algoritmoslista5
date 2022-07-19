#11 
def runLenght(txt):
    if len(txt) == 0 :
        return []
    i = 1
    while i != len(txt) and (txt[0 + i - 1] == txt[1 + i - 1]):
        i += 1 
    atual = [txt[0], i]

    return(atual + runLenght(txt[i:])) 

def main():
    ç = ["A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "B", "B", "B", "B", "A", "A", "A", "A", "A", "A", "B"]
    print(runLenght(ç))
    min = max = 0
    print(min, max)

if __name__ == '__main__':
    main()