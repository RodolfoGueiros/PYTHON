#Adicionar lista
lista = []
def add_lista():
    new_list = (dados1,dados2)
    lista.append(new_list)

#Exibir lista
def show_lista():
    for data_list in show_lista:
        print (data_list)    
    

opcao = 0
while opcao != 3:
    print ('''    (1) Adicionar uma lista
    (2) Exibir a lista
    (3) Sair''')
    opcao = int(input("Escolha sua Opção: "))
    if opcao == 1:
        dados1 = input ("Informe 1 palava: ")
        dados2 = input ("Informe 2 palava: ")
        add_lista()
    elif opcao == 2:
        show_lista()
    elif opcao == 3:
        print("Obrigado e volte sempre!")
print ("___"*10)
print ("Fim da Trivia! Obrigado por jogar!")
        
