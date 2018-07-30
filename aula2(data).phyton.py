'''
Programa para informar quantos dias faltam para o natal
'''

from datetime import date
hoje = date.today()
Days=hoje.toordinal()

pergunta = input ("Informe a data atual neste formato 2000,11,15: ")
print ("Hoje é: " + pergunta)
natal = date(2017,12,25)
diferenca = (pergunta - natal)
print ("Faltam, " + str(diferenca) + " para o natal")
