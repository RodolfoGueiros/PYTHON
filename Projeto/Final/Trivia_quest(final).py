'''
Curso Python
Projeto conclusão:Jogo Trivia
Monitor: Pedro Rossi
Aluno:   Rodolfo Marques
fontes de pesquisa:
    https://goo.gl/mYsSQE
    https://goo.gl/FaetyJ
    https://goo.gl/HjtucD
    https://goo.gl/BtM9A7
'''

from time import sleep
#adiciona na lista
lista = []
def add_trv():
    perg = input ("Digite a pergunta: ")
    resp = input ("Digite a resposta: ")
    trv = ({"pergunta":perg, "resposta":resp}) 
    lista.append(trv)

#Exibe da lista
def del_trv():
    for elemento in lista:
        indice_trv = lista.index(elemento)
        print ("{}) - {}".format(indice_trv, elemento["pergunta"]))

    opcao_selec = input ("Informe o numero da questao que deseja remover ou -1, para voltar: ")
    opcao_selec = int(opcao_selec)

    if opcao_selec > -1:
        del lista[opcao_selec]
        print ("Trivia Removida com Sucesso!")

# Jogar Trivia
score = 0
def play_trv():
    global score
    for elemento in lista:    
        print ("{}".format(elemento["pergunta"]))
        resposta = input ("Resposta: ")

        if resposta == elemento["resposta"]:
            score += 10 

    print ("Seu score total foi {}!".format(score))


print ("Bem vindo ao Trivia Quest !")

opcao = 0
while opcao != 4:
    #Opcoes do menu
    print ("O que você deseja fazer ?")
    print ("(1) Adicionar uma Trivia")
    print ("(2) Remover uma Trivia")
    print ("(3) Jogar")
    print ("(4) Sair")

    opcao = int(input("Opção: "))
    print ("Opção: {}".format(opcao))
    
    if opcao == 1:
        add_trv()
        print (">>>>>>>> Trivia adicionada com sucesso!")
    elif opcao == 2:
        del_trv()
    elif opcao == 3:
        play_trv()
    elif opcao == 4:
        print ("Finalizando... Volte sempre!")
    print ('___'*20)
    sleep(2)
print ("Fim da Trivia! Obrigado por jogar!")

