# Exercicio Funcoes 3

l1=[1,2,3]
l2=[5,8,4]

def list_int (l1,l2):
    resultado = (l1+l2)
    resultado.sort()
    return resultado
teste = list_int(l1,l2)

print (teste)
