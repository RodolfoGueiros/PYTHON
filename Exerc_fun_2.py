# Funcao teste 2

print ("Informe 3 valores inteiros :")

vlr1 = int(input ("Valor 1: "))
vlr2 = int(input ("Valor 2: "))
vlr3 = int(input ("Valor 3: "))

def calc_med (vlr1, vlr2, vlr3):
    soma = vlr1 + vlr2 + vlr3 / 3
    return soma

print (calc_med (vlr1, vlr2, vlr3))
