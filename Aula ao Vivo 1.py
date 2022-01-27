#Exercício 1
print('CALCULADORA DE PREÇO DE GASOLINA')
lit = float(input('Indique quantos litros serão abastecidos: '))
if (lit <= 1):
    val = 7
elif (lit > 1) and (lit <= 10):
    val = 6.5
elif (lit > 10):
    val = 6
else:
    print('Essa não é uma quantidade válida!')

print('Valor total: {}' .format(lit * val))

#Exercício 2
print('PROGRAMA DE PERGUNTAS SOBRE O CRIME')
contador = 0
print('Responda às seguintes questões com S ou N: ')
p1 = input('Telefonou para a vítima? ')
if (p1 == 's') or (p1 == 'S'):
    contador = contador + 1
p2 = input('Esteve no local do crime? ')
if (p2 == 's') or (p2 == 'S'):
    contador = contador + 1
p3 = input('Mora perto da vítima? ')
if (p3 == 's') or (p3 == 'S'):
    contador = contador + 1
p4 = input('Devia para a vítima? ')
if (p4 == 's') or (p4 == 'S'):
    contador = contador + 1
p5 = input('Já trabalhou com a vítima? ')
if (p5 == 's') or (p5 == 'S'):
    contador = contador + 1

if (contador == 2):
    print('Você é suspeito!')
elif (contador == 3) or (contador == 4):
    print('Você é cúmplice!')
elif (contador == 5):
    print('Você é o assassino!')
else:
    print('Você é inocente!')