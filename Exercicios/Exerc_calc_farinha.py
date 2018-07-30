'''
TRANSFORMAR PORCENTAGEM PARA PESO
'''

print("Calcular peso: ") 
farinha=float(input("Informe o peso da farinha: "))
ingrediente=float(input("Informe o porcento do Ingrediente: "))

resultado = float((farinha / 100) * ingrediente)

print("O peso do ingrediente é: " + resultado)
