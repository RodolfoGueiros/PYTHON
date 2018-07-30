'''       Curso Python
   Projeto conclusão:Jogo Trivia

              by, Rodolfo Marques'''

#adiciona na lista
lista = []
def add_trv():
    perg = input ("Digite a pergunta: ")
    resp = input ("Digite a resposta: ")
    trv = (perg, resp) 
    lista.append(trv)

#Exibe da lista
def show_trv():
    for elemento in lista:
        indice_trv = str(lista.index(elemento))
        print ("{} - {}".format(indice_trv, elemento))

    opcao_selec = input ("Informe o numero da questao que deseja remover ou -1, para voltar: ")
    opcao_selec = int(opcao_selec)

    if opcao_selec > -1:
        del lista[opcao_selec]
        print ("Opção: {}".format(opcao_selec))
        print ("Trivia Removida com Sucesso!")

# Jogar Trivia
score = 0
def play_trv():
    from random import randrange
    index = randrange(0,len(lista))
    print (lista[index])

print ("Bem vindo ao Trivia Quest !")

opcao = 0
while opcao != 4:
    print ('''    (1) Adicionar uma Trivia
    (2) Remover uma Trivia
    (3) Jogar
    (4) Sair''')
    opcao = int(input("Escolha sua Opção: "))
    if opcao == 1:
        add_trv()
        print (">>>>>>>>Trivia adicionada com sucesso!")
    elif opcao == 2:
        show_trv()
    elif opcao == 3:
        play_trv()
    print ('___'*20)
print ("Fim da Trivia! Obrigado por jogar!")

