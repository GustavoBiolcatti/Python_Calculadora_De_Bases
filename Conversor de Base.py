import math

while True:
    print("\n")
    print("\033[1;30m-\033[0;0m"*51)
    print("   *** DEIXE VAZIO CASO NÃO DESEJE CONTINUAR ***")
    
    n = input("Digite o número a ser convertido: ").upper().replace(",", ".").strip()
    
    if n == "": break # verifica a condição de paradaa do loop
    
    n_base = int(input("Digite a base do número: "))
    
    print("\n")
    
    letra = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F", 16: "G", 17: "H", 18: "I", 19: "J", 20: "K",
                   "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15, "G": 16, "H": 17, "I": 18, "J": 19, "K": 20}
    
    letraFora16 = ["G", "H", "I", "J", "K", "L", "M", "O", "N", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    
    # +=========================================================================+ #
    # |                                  FUNÇÕES                                | #
    # +=========================================================================+ #
    
    def removeZero(lista):
        while lista[0] == 0:
            lista.remove(0) # se houver, remove os números '0' do começo do binário
        
        return lista
    
    # Converte os valores para Binário (Base 2)
    def converteBase2(num, num_base):
        base2 = []
        
        if num_base == 10:
            if "." in n: # converte um 'float'
                int_base2 = []
                dec_base2 = []
                
                verif_rep = []
                
                intr = int(n.split(".")[0])
                dec = int(n.split(".")[1]) / 10**len(n.split(".")[1])
                
                while True: # cálculo da parte inteira - antes da vírgula
                    if intr >= 2:
                        resto = intr % 2
                        int_base2.append(math.trunc(resto))
                        
                        intr = intr / 2
                    else:
                        int_base2.append(math.trunc(intr))
                        int_base2 = int_base2[::-1]
                        break
                
                while dec > 0: # cálculo da parte decimal - depois da vírgula
                    dec = dec * 2
                    
                    if len(verif_rep) > 4:
                        verif_rep.clear()
                    else:
                        verif_rep.append(int(str(dec)[0]))
                    
                    dec_base2.append(int(str(dec)[0]))
                    
                    if dec >= 1:
                        dec -= 1
                
                # organiza o vetor de exibição - base2
                for i in int_base2:
                    base2.append(i)
                
                if base2 is None:
                    base2.append(0)
                
                base2.append(".")
                
                for i in dec_base2:
                    base2.append(i)
                    
            else:
                val = int(n)
                
                while True:
                    if val >= 2:
                        resto = val % 2
                        base2.append(math.trunc(resto))
                        
                        val = val / 2
                    else:
                        base2.append(math.trunc(val))
                        base2 = base2[::-1]
                        break
                
        elif  num_base == 8:
            val = n
            
            if "." in num:
                pass
            else:
                for num in val:
                    i = 2
                    while i >= 0:
                        num = int(num)
                        if (num - 2**i) >= 0:
                            num = num - 2**i
                            base2.append(1)
                        else:
                            base2.append(0)
                            
                        i -= 1
        
        elif num_base == 16:
            val = list(n)
            n_val = []
            
            if "." in num:
                pass
            else:
                for i in range(0, len(val), 1): # substitui as letras por número
                    if not val[i].isnumeric():
                        n_val.append(letra[val[i]])
                    else:
                        n_val.append(val[i])
                
                for num in n_val:
                    i = 3
                    while i >= 0:
                        num = int(num)
                        if (num - 2**i) >= 0:
                            num = num - 2**i
                            base2.append(1)
                        else:
                            base2.append(0)
                            
                        i -= 1
        
        return removeZero(base2)
    
    # Converte os valores para Decimal (Base 10)
    def converteBase10(num, num_base):
        base10 = 0
        i = 0
        
        if num_base == 2:
            val = 0
            
            if "." in num:
                pass
            else:
                for n in num[::-1]:
                    base10 += int(n) * 2**i
                    i += 1
        
        if num_base == 8:
            val = n
            i = 0
            
            if "." in num:
                pass
            else:
                for num in val[::-1]:
                    base10 += int(num) * (8**i)
                    i += 1
        
        elif num_base == 16:
            val = list(num)
            i = 0
            
            if "." in num:
                pass
            else:
                for num in val[::-1]:
                    if num.isnumeric():
                        num = int(num)
                    else:
                        num = letra[num]
                    
                    base10 += int(num) * (16**i)
                    i += 1
    
        return base10
    
    # Converte os valores para Octal (Base 8)
    def converteBase8(num, num_base):
        base8 = []
        
        if "." in num:
            pass
        else:
            if num_base != 10:
                val = converteBase10(num, num_base)
            else:
                val = int(num)
                
            while True:
                if val >= 8:
                    resto = val % 8
                    base8.append(math.trunc(resto))
                    
                    val = val / 8
                else:
                    base8.append(math.trunc(val))
                    base8 = base8[::-1]
                    break
            
        return base8
    
    # Converte os valores para Hexadecimal (Base 16)
    def converteBase16(num, num_base):
        base16 = []
        
        if "." in num:
            pass
        else:
            if num_base != 10:
                val = converteBase10(num, num_base)
            else:
                val = int(num)
            
            while True:
                if val >= 16:
                    resto = val % 16
                    if resto < 10:
                        base16.append(math.trunc(resto))
                    else:
                        base16.append(letra[math.trunc(resto)])
                    
                    val = val / 16
                else:
                    if val < 10:
                        base16.append(math.trunc(val))
                    else:
                        base16.append(letra[math.trunc(val)])
                    
                    base16 = base16[::-1]
                    break
        
        return base16
    
    # +=========================================================================+ #
    # |                                 EXIBIÇÃO                                | #
    # +=========================================================================+ #
    
    if n_base == 2:
        print("BASE 2: ",  n)
        print("BASE 8:  ", *converteBase8(n, n_base), sep="")
        print("BASE 10:",  converteBase10(n, n_base))
        print("BASE 16: ", *converteBase16(n, n_base), sep="")
    
    elif n_base == 10:
        print("BASE 2:  ", *converteBase2(n, n_base), sep="")
        print("BASE 8:  ", *converteBase8(n, n_base), sep="")
        print("BASE 10:",  n)
        print("BASE 16: ", *converteBase16(n, n_base), sep="")
        
    elif n_base == 8:
        print("BASE 2:  ", *converteBase2(n, n_base), sep="")
        print("BASE 8: ",  n)
        print("BASE 10:",  -converteBase10(n, n_base))
        print("BASE 16: ", *converteBase16(n, n_base), sep="")
             
    elif n_base == 16:
        
        for i in n:
            if i in letraFora16:
                print("O valor não corresponde à base hexadecimal".format(i))
                verif_valorBase = False
                break
        
        if verif_valorBase == False:
            break
                
        print("BASE 2:  ", *converteBase2(n, n_base), sep="")
        print("BASE 8:  ", *converteBase8(n, n_base), sep="")
        print("BASE 10:", converteBase10(n, n_base))
        print("BASE 16:", n)
