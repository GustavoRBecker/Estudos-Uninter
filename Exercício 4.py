#O programa começa importando as bibliotecas necessárias e definindo a função seed

from random import seed
from random import randint
seed(100)

#Esta é a função responsável por cadastrar os alunos na lista

def cadastro(nome,email,telefone,curso):
    while True:
        Aluno['Voucher'] = randint(100, 400)
        Aluno['Nome'] = input(nome)
        Aluno['Email'] = input(email)
        Aluno['Telefone'] = int(input(telefone))
        Aluno['Curso'] = input(curso)
        Alunos.append(Aluno.copy())

#Aqui a função perguntará se o usuário deseja cadastrar outro aluno

        try:
            sn = input('Deseja cadastrar outro aluno? [s/n]')
            if sn in 'sS':
                continue
            elif sn in 'nN':
                break

#Caso seja selecionada uma opção inválida, o usuário será enviado ao menu principal

        except:
            print('Opção inválida, retornando ao menu principal')
            break

#Este é o início do programa principal

#Aqui definimos a lista Alunos e o dicionário Aluno como globais para poderem ser alteradas dentro da função

global Alunos
global Aluno
Alunos = []
Aluno = {}
while True:

#Este é o menu principal

    print('Programa de cadastro para cursos grátis')
    print('|',('-'*17),'MENU',('-'*17),'|')
    print('Inscrição: [1]\nVisualizar Inscrições: [2]\nEncerrar: [0]')
    try:
        opcao = int(input('Selecione uma opção:'))

#Caso selecione a opção Inscrição, o programa chamará a função cadastro

        if (opcao == 1):
            cadastro('Digite o nome do usuário: ','Digite o email: ','Digite o telefone: ','Digite o curso: ')

#Caso selecione a opção Visualizar Inscrições, o programa irá imprimir na tela a lista de alunos um a um

        elif (opcao == 2):
            if (len(Alunos) >= 1):
                print('|',('-' * 4),'Alunos inscritos',('-' * 4),'|')
                for i, j in Aluno.items():
                    print('{}: {}' .format(i,j))

#Caso a lista de inscrições esteja vazia, o programa exbirá uma mensagem e retornará ao menu principal

            else:
                print('Nenhuma inscrição cadastrada! Retornando ao menu...')
                continue

#Caso o usuário escolha a opção Encerrar, o programa findará sua execução

        elif (opcao == 0):
            print('Encerrando...')
            break

#Caso o usuário selecionar uma opção que não esta listada, o programa exibirá uma mensagem e retornará ao menu principal

    except:
        print('Opção inválida, tente novamente.')
        continue