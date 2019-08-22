import math

n = int(input("Digite o número a ser convertido: "))
n_base = int(input("Digite a base do número: "))

base2 = []

if n_base == 10:
    # DECIMAL PARA BINÁRIO
    div = n
    while True:
        if div >= 2:
            resto = div % 2
            base2.append(math.trunc(resto))
            
            div = div / 2
        else:
            break

    base2.append(math.trunc(div))
    base2 = base2[::-1]
    
print(base2)
