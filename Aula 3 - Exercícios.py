print(2 + 2 < 4)

print(7 // 3 == 1 + 1)

print(3 ** 2 + 4 ** 2 == 25)

print(2 + 4 + 6 > 12)

if (1387 % 19 == 0):
    print('1387 é divisível por 19')

if (31 % 2 == 0):
    print('31 é par')
else:
    print('31 é ímpar')

if (min(34, 29, 31) < 30):
    print('O menor valor entre 34, 29 e 31 é menor que 30')

idade = int(input('Digite sua idade: '))
if (idade > 60):
    print('Você tem direito aos benefícios.')

dano = int(input('Digite quanto de dano você tomou: '))
escudo = int(input('Digite quanto você tem de escudo: '))
if (dano > 10 and escudo == 0):
    print('Você está morto!')

if (idade > 60):
    print('Você tem direito aos benefícios!')

if (dano > 10 and escudo == 0):
    print('Você está morto!')

if ('norte' or 'sul' or 'leste' or 'oeste'):
    print('Você escapou!')

#Exercícios condicional composta
if (dano % 4 == 0):
    print('Pode ser um ano bissexto.')
else:
    print('Definitivamente não é um ano bissexto.')

if (cima and baixo):
    print('Decida-se!')
else:
    print('Você escolheu um caminho')

print('Digite o tamanho dos lados de um triângulo:')
lado1 = int(input('Digite o valor do primeiro lado: '))
lado2 = int(input('Digite o valor do segundo lado: '))
lado3 = int(input('Digite o valor do terceiro lado: '))
if (lado1 <= 0) or (lado2 <= 0) or (lado3 <= 0) or (lado1 + lado2 > lado3) or (lado1 + lado3 > lado2) or (lado2 + lado3 > lado1):
    print('Não pode ser um triângulo!')
else:
    print('Esse tipo de triângulo é chamado de:')
    if (lado1 == lado2 == lado3):
        print('Equilátero')
    elif (lado1 == lado2 != lado3) or (lado1 == lado3 != lado2) or (lado2 == lado3 != lado1):
        print('Isósceles')
    else:
        print('Escaleno')

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
print('Soma - +')
print('Subtração - -')
print('Mutliplicação - *')
print('Divisão - /')
op = input('Digite o símbolo da operação desejada: ')
if (op == '+'):
    res = n1 + n2
    print('{}'.format(res))
elif (op == '-'):
    res = n1 - n2
    print('{}'.format(res))
elif (op == '*'):
    res = n1 * n2
    print('{}'.format(res))
elif (op == '/'):
    res = n1 / n2
    print('{}'.format(res))
else:
    print('Essa não é uma operação válida!')

print('PREÇO A PAGAR ENERGIA ELÉTRICA')
kw = int(input('Digite quantos kWh foi consumido: '))
print('R - Residências')
print('I - Indústrias')
print('C - Comércios')
tipo = input('Informe o tipo de instalação (Utilize a primeira letra): ')

if (tipo == 'R'):
    if (kw <= 500):
        pre = kw * 0.40
        print('Tipo de instalação: {}; kWh consumidos: {}; Total à pagar: {}.' .format(tipo, kw, pre))
    else:
        pre = kw * 0.65
        print('Tipo de instalação: {}; kWh consumidos: {}; Total à pagar: {}.' .format(tipo, kw, pre))
elif (tipo == 'I'):
    if (kw <= 5000):
        pre = kw * 0.55
        print('Tipo de instalação: {}; kWh consumidos: {}; Total à pagar: {}.' .format(tipo, kw, pre))
    else:
        pre = kw * 0.60
        print('Tipo de instalação: {}; kWh consumidos: {}; Total à pagar: {}.' .format(tipo, kw, pre))
elif (tipo == 'C'):
    if (kw <= 1000):
        pre = kw * 0.55
        print('Tipo de instalação: {}; kWh consumidos: {}; Total à pagar: {}.' .format(tipo, kw, pre))
    else:
        pre = kw * 0.60
        print('Tipo de instalação: {}; kWh consumidos: {}; Total à pagar: {}.' .format(tipo, kw, pre))
else:
    print('Não é um tipo de instalação válida!')