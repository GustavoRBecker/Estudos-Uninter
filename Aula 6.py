import math

print(math.sqrt(9))

notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]
print(notas.count(7))
notas[-1] = 4
print(notas)
maior = 0
for i in notas:
    if (i > maior):
        maior = i
print(maior)
notas.sort()
print(notas)
soma = 0
for i in notas:
    soma += i
print(soma / len(notas))

palavras = ('casa','cachorro','jujuba','gatinho','pereba','boletim','cadarço','mouse','celular','andaime')
for palavra in palavras:
    print('\nPalavra: {}. Vogais: ' .format(palavra.upper()), end = '')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra.upper(), end = ' ')

import random

def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

def vencedor(jogador1, jogador2):
    global empate, v1, v2
    if jogador1 == 1:
        if jogador2 == 1:
            empate += 1
        elif jogador2 == 2:
            v2 += 1
        elif jogador2 == 3:
            v1 += 1
    elif jogador1 == 2:
        if jogador2 == 1:
            v1 += 1
        elif jogador2 == 2:
            empate += 1
        elif jogador2 == 3:
            v2 += 1
    elif jogador1 == 3:
        if jogador2 == 1:
            v2 += 1
        elif jogador2 == 2:
            v1 += 1
        elif jogador2 == 3:
            empate += 1
    resultados = [v1, v2, empate]
    return resultados

print('JOKENPO')
print('1 - Pedra')
print('2 - Papel')
print('3 - Tesoura')

resultado = []
jogadas = []
v1 = 0
v2 = 0
empate = 0

while True:
    j1 = valida_int('Escolha sua jogada: ', 0, 3)
    if not j1 :
        break
    j2 = random.randint(1, 3)
    jogadas.append([j1, j2])
    resultados = vencedor(j1, j2)

    for jogada in jogadas:
        for dado in jogada:
            print(dado, end=' ')
        print()

print('Número de vitórias do jogador 1: {}' .format(resultados[0]))
print('Número de vitórias do jogador 2: {}' .format(resultados[1]))
print('Número de empates: {}' .format(resultados[2]))

cadastro = {'nome':[],'sexo':[],'ano':[]}
mulhermenos30 = {'nome':[],'sexo':[],'ano':[]}
homemidademedia = {'nome':[],'sexo':[],'ano':[]}

while True:
    terminar = input('Deseja cadastrar uma pessoa? [S/N}')
    if terminar.upper() in 'N':
        break
    if terminar.upper() not in 'S':
        print('Digite S para SIM ou N para NÃO')
        continue

    nome = input('Qual seu nome? ')
    sexo = input('Qual seu sexo? [M/F]')
    ano = int(input('Qual seu ano de nascimento? '))
    if (sexo.upper() == 'F') and (ano > 1991):
        mulhermenos30['nome'].append(nome)
        mulhermenos30['sexo'].append(sexo.upper())
        mulhermenos30['ano'].append(ano)
    cadastro['nome'].append(nome)
    cadastro['sexo'].append(sexo.upper())
    cadastro['ano'].append(ano)

print('Total de cadastros efetuados: {}' .format(len(cadastro['nome'])))
somaidade = 0
mediaidade = 0
qtdpessoas = len(cadastro['ano'])
for i in (cadastro['ano']):
    idadecada = 2021 - i
    somaidade += idadecada
mediaidade = (somaidade / qtdpessoas)
print('Média de idades cadastradas: {}' .format(mediaidade))
print('Mulheres com menos de 30 anos: {}') .format(mulhermenos30)

for i in cadastro['sexo']:
    if (i.upper() == 'M'):
        for j in cadastro['ano']:
            if ((2021 - j) > mediaidade):
                homemidademedia.append(cadastro)
print('Homens com idade acima da média: {}' .format(homemidademedia))