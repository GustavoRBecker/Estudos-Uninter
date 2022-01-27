#Fazendo uma docstring:

def soma(x = 0, y = 0, z = 0):
    """
    Função que soma até 3 valores inteiros
    :param x: valor inteiro opcional
    :param y: valor inteiro opcional
    :param z: valor inteiro opcional
    :return: soma inteira
    """
    return x+y+z

print(soma(2, 3))
help(soma)

#Exercício 1:

def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        print('Valor não suportado')
        x = int(input(pergunta))
    return x

def fatorial(num):
    fat = 1
    if num == 0:
        return fat
    for i in range(1, num+1, 1):
        fat *= i
    return fat

x = valida_int('Digite um valor para calcular a fatorial: ', 0, 99999)
print('Fatorial de: {}! = {}' .format(x, fatorial(x)))

#Exercício 2:
def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        print('Valor não suportado')
        x = int(input(pergunta))
    return x

def criaArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+')
        a.close()
    except:
        print('Erro na criação do arquivo')
    else:
        print('Arquivo {} foi criado com sucesso!\n' .format(nomeArquivo))

def existeArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def listarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        print(a.read())
    finally:
        a.close()

def cadJogo(nomeArquivo, n, p):
    try:
        a = open(nomeArquivo, 'at')
    except:
        print('Erro ao abrir o arquivo')
    else:
        a.write('{};{}\n' .format(n,p))
    finally:
        a.close()

arquivo = 'games.txt'
if existeArquivo(arquivo):
    print('Arquivo encontrado')
else:
    print('Arquivo inexistente')
    criaArquivo(arquivo)

while True:
    print('MENU')
    print('Cadastrar novo jogo: 1\nLista de jogos cadastros: 2\nSair: 3')
    menu = valida_int('Escolha uma das opções: ', 1, 3)
    if menu == 1:
        print('Opção de cadastrar novo item, selecionada:\n')
        n = input('Digite o nome do jogo: ')
        p = input('Digite a plataforma do jogo: ')
        cadJogo(arquivo, n, p)
    elif menu == 2:
        print('Opção de abrir catálogo, selecionada:\n')
        listarArquivo(arquivo)
    elif menu == 3:
        print('Encerrando o programa...')
        break

def realce(s1):
    print('|','__' * 10,'|')
    print('|','__' * 10,'|')
    print(s1)
    print('|', '__' * 10, '|')
    print('|', '__' * 10, '|')

realce('          MENU')

def sub2(x, y):
    res = x - y
    print(res)

sub2(5, 3)
sub2(45, 32)

def soma3(x, y, z):
    res = x + y + z
    print(res)

soma3(4, 5, 8)
soma3(7, 5, 3)

def soma3(x = 0, y = 0, z = 0, imprime = False):
    res= x + y + z
    if imprime:
        print(res)

soma3(2, 6, 8, True)
soma3(4, 7, imprime = True)

def nome(escrito):
    tam = len(escrito)
    if tam:
        print('+', '-' * tam, '+')
        print('|',escrito,'|')
        print('+', '-' * tam, '+')

nome('Gustavo')

def cont(fin, ini = 0, pas = 1):
    for i in range(ini, fin, pas):
        print('{} ' .format(i + 1), end = '')
    print('\n')

cont(8)
cont(15, 5, 3)

def crescente(x = 0, y = 0, z = 0):
    if (x > y) and (x > z):
        if (y > z):
            print('Valores {}; {}; {}.' .format(z,y,x), end='')
        else:
            print('Valores {}; {}; {}.' .format(y,z,x), end='')
    if (y > x) and (y > z):
        if (x > z):
            print('Valores {}; {}; {}.' .format(z,x,y), end='')
        else:
            print('Valores {}; {}; {}.' .format(x,z,y), end='')
    if (z > x) and (z > y):
        if (x > y):
            print('Valores {}; {}; {}.' .format(y,x,z), end='')
        else:
            print('Valores {}; {}; {}.' .format(x,y,z), end='')

x = int(input('Digite um número: '))
y = int(input('Digite outro número: '))
z = int(input('Digite mais um número: '))
crescente(x,y,z)

def string(frase, min, max):
    tam = len(frase)
    if (tam < min) or (tam > max):
        return False
    else:
        return True

frase = input('Digite uma frase entre 10 a 20 caracteres: ')
while string(frase, 10, 20) == False:
    frase = input('Digite uma frase entre 10 a 20 caracteres: ')
print(frase)

def validafat(num, min):
    x = int(input(num))
    while (x < min):
        x = int(input(num))
    return x

def calc(num):
    fat = 1
    if (num == 0):
        return fat
    for i in range(1, num+1, 1):
        fat *= i
    return fat

resultado = validafat('Digite um número para obter seu fatorial: ', 0)
print('Número: {}. Fatorial: {}!' .format(resultado,calc(resultado)))

def validasoma(num,inicio,final):
    x = int(input(num))
    while (x < inicio) or (x > final):
        x = int(input(num))
    return x

def soma(x, y):
    total = 0
    for i in range(x, y+1):
        total += i
    return total

x = validasoma('Digite um número: ', 1, 99999)
y = validasoma('Digite outro número: ', 1, 99999)
print('Números: {} e {}. Soma: {}' . format(x,y,soma(x,y)))

x = int(input('Digite um número: '))
y = 6

res = x * y
print(res)