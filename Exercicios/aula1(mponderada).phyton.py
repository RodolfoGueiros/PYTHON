#Media Ponderada em Python
# Pesos das notas 3, 5 e 7



nota1 = input ("Informe primeira nota: ")
nota2 = input ("Informe segunda nota: ")
nota3 = input ("Informe terceira nota: ")

nota1 = float(nota1)
nota2 = float(nota2)
nota3 = float(nota3)

peso1 = input ("Informe peso1: ")
peso2 = input ("Informe peso2: ")
peso3 = input ("Informe peso3: ")

peso1 = int(peso1)
peso2 = int(peso2)
peso3 = int(peso3)

media = ((nota1*peso1)+(nota2*peso2)+(nota3*peso3))/(peso1+peso2+peso3)

print (media)
