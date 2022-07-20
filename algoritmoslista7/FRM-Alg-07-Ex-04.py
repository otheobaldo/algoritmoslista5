# 4.

def morseCode(txt):
    txt_morse = ""
    morse = {"A":".-", "B":"-...", "C":"-.-.", "D":"-..", "E":".", "F":"..-.", "G":"--.", "H":"....", "I":"..", "J":".---", "K":"-.-", "L":".-..", "M":"--", "N":"-.", "O":"---", "P":".--.", "Q":"--.-", "R":".-.", "S":"...", "T":"-", "U":"..-", "V":"...-", "W":".--", "X":"-..-", "Y":"-.--", "Z":"--..", "0":"-----", "1":".----", "2":"..---", "3":"...--", "4":"....-", "5":".....", "6":"-....", "7":"--...", "8":"---..", "9":"----.",}
    for c in txt:
        if c.isalpha() == True:
            d = morse[c.upper()]
            txt_morse = txt_morse + d + " "
        elif c.isnumeric() == True:
            d = morse[c]
            txt_morse = txt_morse + d + " "

    return(txt_morse)

def main():
    frase = input("Digite uma frase: ")
    x = morseCode(frase)
    print(x)

if __name__ == '__main__':
    main()