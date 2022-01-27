#Exemplo:

#Letra a:
x = 3
while x < 13:
    print(x)
    x += 1

for i in range (3,13,1):
    print(i)

#Letra b:
x = 0
while x < 9:
    if x % 2 == 0:
        print(x)
    x += 1

for i in range (0,9,2):
    print(i)

#Exercício 1:
op = ''
while op != 's':
    print('CALCULADORA')
    x = float(input('Digite um valor numérico qualquer: '))
    y = float(input('Digite outro valor numérico qualquer: '))
    print('Adição: +')
    print('Subtração: -')
    print('Multiplicação: *')
    print('Divisão: /')
    print('Sair: s')
    op = input('Escolha uma operação ou sair: ')
    if op == '+':
        res = x + y
    elif op == '-':
        res = x - y
    elif op == '*':
        res = x * y
    elif op == '/':
        res = x / y
    elif op == 'sair':
        break
    else:
        print('Operação Inválida!')
    print('{} {} {} = {}' .format(x,op,y,res))

#Exercício 2:

contador100 = 0
contador50 = 0
contador20 = 0
contador10 = 0
contador5 = 0
contador1 = 0
x = int(input('Digite um valor: '))
while x >= 100:
    x -= 100
    contador100 += 1
    while x >= 50:
        x -= 50
        contador50 += 1
        while x >= 20:
            x -= 20
            contador20 += 1
            while x >= 10:
                x -= 10
                contador10 += 1
                while x >= 5:
                    x -= 5
                    contador5 += 1
                    while x >= 1:
                        x -= 1
                        contador1 += 1
print ('{} notas de 100, {} notas de 50, {} notas de 20, {} notas de 10, {} notas de 5 e {} notas de 1.' .format(contador100,contador50,contador20,contador10,contador5,contador1))

#Exercício 3:

print('Programa de venda de ingressos!')
pessoas = 0
totalid = 0
preco = 0
while True:
    id = input('Digite a idade do usuário do ingresso ou (s) para sair: ')
    if id == 's':
        break
    id = int(id)
    pessoas += 1
    totalid += id
    if id < 3:
        print('Idade do usuário: {}. Ingresso gratuito.' .format(id))
        preco += 0
    elif id >= 3 and id <= 12:
        print('Idade do usuário: {}. Valor do ingresso: 15 reais.' .format(id))
        preco += 15
    elif id > 12:
        print('Idade do usuário: {}. Valor do ingresso: 30 reais.' .format(id))
        preco += 30
    else:
        print('Valor inválido!')
        continue

if pessoas != 0:
    print('Total de ingressos: {}' .format(pessoas))
    print('Preço final: {}' .format(preco))
    print('Média de idades: {}' .format(totalid / pessoas))

x = 10
while (x <= 1000):
    print(x)
    x += 1

x = 10
while (x >= 0):
    print(x)
    x -= 1
print('Fogo!')

x = int(input('Digite um valor inicial: '))
y = int(input('Digite um valor final: '))
if (x % 2 != 0):
    x += 1
while (x <= y):
    print(x)
    x += 2

x = 3
y = 1
res = x * y
while (res < 3 * 10):
    print(res)
    y += 1
    res = x * y

y = 1
print('Escolha um número que lhe darei sua tabuada')
x = int(input('Digite o número: '))
while (y <= 10):
    res = x * y
    print('{}X{}={}' .format(y,x,res))
    y += 1

soma = 0
cont = 1
print('Digite 5 valores para somarmos!')
while (cont <= 5):
    x = int(input('Digite o {} valor: ' .format(cont)))
    soma += x
    cont += 1
media = soma / 5
print('Soma total dos valores: {}\nMédia: {}' .format(soma, media))

soma = 0
x = int(input('Digite um valor: '))
y = int(input('Digite outro valor: '))
while (y > 0):
    soma += x
    y -= 1
print(soma)

print('Digite um valor inicial e um final!')
x = int(input('Valor inicial: '))
y = int(input('Valor final: '))
qtd_par = 0
qtd_impar = 0
qtd_pos = 0
soma_par = 0
soma_impar = 0
soma_pos = 0
cont = x
if (x < y):
    while (cont <= y):
        if (cont > 0):
            qtd_pos += 1
            soma_pos += cont
        if (cont % 2 == 0):
            qtd_par += 1
            soma_par += cont
        else:
            qtd_impar += 1
            soma_impar += cont
        cont += 1
else:
    print('Você digitou um valor inválido')

media_pos = soma_pos / qtd_pos
media_par = soma_par / qtd_par
media_impar = soma_impar / qtd_impar

print('Números positivos e inteiros: {}. Valor médio: {}.' .format(qtd_pos,media_pos))
print('Números pares: {}. Valor médio: {}.' .format(qtd_par,media_par))
print('Números ímpares: {}. Valor médio: {}.' .format(qtd_impar,media_impar))

print('Digite um valor inicial e um final!')
x = int(input('Valor inicial: '))
y = int(input('Valor final: '))
qtd_pos = 0
qtd_par = 0
qtd_impar = 0
soma_pos = 0
soma_par = 0
soma_impar = 0
cont = x
if (x < y):
    while (cont <= y):
        if (cont > 0):
            qtd_pos += 1
            soma_pos += cont
        if (cont % 2 == 0):
            qtd_par += 1
            soma_par += cont
        else:
            qtd_impar += 1
            soma_impar += cont
        cont += 1

    media_pos = soma_pos / qtd_pos
    media_par = soma_par / qtd_par
    media_impar = soma_impar / qtd_impar
    print('Números positivos: {}. Valor médio: {}.' .format(qtd_pos,media_pos))
    print('Números pares: {}. Valor médio: {}.'.format(qtd_par, media_par))
    print('Números ímpares: {}. Valor médio: {}.'.format(qtd_impar, media_impar))

else:
    print('Valores não permitidos!Encerrando...')

soma = 0
qtd = 0
x = 0
print('Digite números positivos para obter a média ou zero para finalizar: ')
while True:
    x = int(input('Digite o número: ' .format(qtd)))
    if (x < 0):
        continue
    if (x == 0):
        break
    else:
        soma += x
        qtd += 1
print('Valor médio: {}.' .format(soma / qtd))

print('Digite valores para calcular a média, ou 0 para finalizar')
qtd = 0
soma = 0
x = 0
while True:
    x = int(input('Digite um número inteiro: '))
    if (x < 0):
        print('Valor inválido')
        continue
    if (x == 0):
        print('Calculando resultado...')
        break
    else:
        soma += x
        qtd += 1

print('Valor médio: {}' .format(soma / qtd))

for i in range(6):
    print(i)

for i in range(1, 6, 1):
    print(i)

for i in range(10, 0, -2):
    print(i)

for i in range(1, 1001):
    print(i)

for i in range(10, -1, -1):
    print(i)
print('Fogo!')

frase = input('Digite uma frase: ')
for i in range(0, len(frase), 1):
    print(frase[i], end='')

media = 0
cont = 0
for i in range(1, 101):
    if (i % 2 == 0):
        media += i
        cont += 1
print(media / cont)

print('Digite um número para exibir sua tabuada.\nEm seguida digite um multiplicador final.')
x = int(input('Número: '))
y = int(input('Multiplicador: '))
for i in range(1, y + 1, 1):
    print('{}X{}={}' .format(x,i,x * i))

print('Digite um número para calcular sua tabuada e em seguida em qual multiplicador deseja parar!')
x = int(input('Digite o número: '))
y = int(input('Digite o multiplicador: '))
for i in range(1,y + 1):
    print('{}X{}={}' .format(x,i,x * i))

num = 1
while (num <= 10):
    multi = 1
    print('Tabuada do {}' .format(num))
    while (multi <= 10):
        print('{}X{}={}' .format(num,multi, num * multi))
        multi += 1
    num += 1

for num in range(1, 11):
    print('TABUADA DO {}!' .format(num))
    for multi in range(1, 11):
        print('{} X {} = {}' .format(num,multi,num*multi))

num = 1
while (num <= 10):
    print('TABUADA DO {}' .format(num))
    for multi in range(1, 11):
        print('{} X {} = {}' .format(num,multi,num*multi))
    num += 1

for num in range(1, 11):
    print('TABUADA DO {}' .format(num))
    multi = 1
    while (multi <= 10):
        print('{} X {} = {}' .format(num,multi,num*multi))
        multi += 1

while True:
    nome = input('Digite seu sexo (M/F): ')
    idade = int(input('Digite sua idade: '))
    if (idade < 0):
        break
    if (nome == 'm') or (nome == 'M'):
        print('Boa noite, Senhor. Sua idade é {}' .format(idade))
    elif (nome == 'f') or (nome == 'F'):
        print('Boa noite, Senhora. Sua idade é {}' .format(idade))
    else:
        print('Sexo inválido!')
        continue

for num in range(2, 100):
    flag = 0
    for i in range(2, num):
        if (num % i == 0):
            flag = 1
            break
    if(not flag):
        print(num)

h_inic = int(input('Digite uma hora inicial: '))
h_fin = int(input('Digite uma hora final: '))
while (h_inic < 0) or (h_inic > h_fin) or (h_inic > 23) or (h_fin > 23) or (h_fin < 0):
    h_inic = int(input('Digite uma hora inicial: '))
    h_fin = int(input('Digite uma hora final: '))
for h in range(h_inic,h_fin):
    for m in range(0, 60):
        for s in range(0,60):
            print(h,':',m,':',s,'h')

while True:
    frase = input('Digite uma frase entre 10 e 30 caracteres: ')
    if (len(frase) < 10) or (len(frase) > 30):
        continue
    else:
        print('Com espaços: {}' .format(frase))
        print('Sem espaços: ', end ='')
        for i in range(0, len(frase)):
            if (frase[i] != ' '):
                print(frase[i], end ='')
        break