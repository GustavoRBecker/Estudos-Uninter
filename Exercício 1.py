#Este é o inicio do programa com a tela inicial
print('PROGRAMA DE CLASSIFICAÇÃO DE ETAPA DE ENSINO')

#O programa começa pedindo os dados de nome e idade da criança
while True:
    nome = input('Digite o nome da criança: ')
    id = int(in1put('Digite a idade da criança: '))

    #Neste próximo passo o programa irá detectar em qual classificação se encaixa a criança
    if id >= 1 and id <=5:
        etapa = 'Educação Infantil'
    elif id >=6 and id <= 10:
        etapa = 'Ensino Fundamental I'
    elif id >= 11 and id <= 14:
        etapa = 'Ensino Fundamental II'
    elif id >=15:
        etapa = 'Ensino Médio'
    else:
        print('Dados inválidos!')
        continue

    #Agora o programa irá informar ao usuário a classificação da criança
    print('Nome da criança: {}. Idade: {}. Classificação: {}' .format(nome, id, etapa))

    #Nesta etapa o programa perguntará se o usuário deseja continuar o programa ou finalizá-lo
    cs = input('Digite (S) para sair ou qualquer outra tecla para tentar novamente: ')
    if cs == 'S' or cs == 's':
        break