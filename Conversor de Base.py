import math

n = int(input("Digite o número a ser convertido: "))
n_base = 10 # n_base = int(input("Digite a base do número: "))

base2 = []
base8 = []
base10 = []
base16 = []

letra_base16 = {9: 9, 10: "A",
                11: "B",
                12: "C",
                13: "D",
                14: "E",
                15: "F"}

# =========================================================================== #

if n_base == 10:
    # DECIMAL PARA BINÁRIO
    div = n
    while True:
        if div >= 2:
            resto = div % 2
            base2.append(math.trunc(resto))
            
            div = div / 2
        else:
            base2.append(math.trunc(div))
            base2 = base2[::-1]
            break
    
    # DECIMAL PARA OCTAL
    div = n
    while True:
        if div >= 8:
            resto = div % 8
            base8.append(math.trunc(resto))
            
            div = div / 8
        else:
            base8.append(math.trunc(div))
            base8 = base8[::-1]
            break
    
    # DECIMAL PARA HEXADECIMAL
    div = n
    while True:
        if div >= 16:
            resto = div % 16
            if resto < 10:
                base16.append(math.trunc(resto))
            else:
                base16.append(letra_base16[math.trunc(resto)])
            
            div = div / 16
        else:
            if div < 10:
                base16.append(math.trunc(div))
            else:
                base16.append(letra_base16[math.trunc(div)])
            
            base16 = base16[::-1]
            break
    
    print("BASE 2:  ", base2)
    print("BASE 8:  ", base8)
    print("BASE 16: ", base16)
