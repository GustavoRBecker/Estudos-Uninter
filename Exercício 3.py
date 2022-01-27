# Aqui esta a função que mostra o mapa das fases

def imprimeMapa(local):
    print('Posições:')
    print('([1], [2], [3], [4])\n([5], [6], [7], [8])')
    print('Quartos:')
    print(local[:4])
    print(local[4:])
    print('Legenda:\n[*] = quarto ocupado\n[ ] = quarto livre\n[G] = quarto ocupado por gato\n[R] = quarto ocupado por rato\n[O] = quarto ocupado por osso\n[Q] = quarto ocupado por queijo\n[C] = quarto ocupado por cão')

#Aqui o programa define a função da primeira fase

def fase1(rato,gato):

#Aqui o programa chama a função do mapa da fase

    local = ('*','*',' ','G','R',' ','*','*')
    imprimeMapa(local)

    #Aqui o usuário define onde colocará os hóspedes

    r = int(input(rato))
    g = int(input(gato))

    #Aqui o programa irá conferir se os hóspedes foram colocados nos locais corretos e irá retornar True caso o usuário tenha acertado e False caso tenha errado

    if r == 6:
        if g == 3:
            print('Sucesso! Próxima fase desbloqueada!')
            return True
        else:
            print('Você perdeu!')
            return False
    else:
        print('Você perdeu!')
        return False

#Aqui o programa define a função da segunda fase

def fase2(cao1,cao2,osso):

# Aqui o programa chama a função do mapa da fase

    local = ' ','*','*','*','*','C',' ',' '
    imprimeMapa(local)

    # Aqui o usuário define onde colocará os hóspedes

    int(input(cao1))
    int(input(cao2))
    os = int(input(osso))

# Aqui o programa irá conferir se os hóspedes foram colocados nos locais corretos e irá retornar True caso o usuário tenha acertado e False caso tenha errado

    if (os == 1):
        print('Sucesso! Próxima fase desbloqueada!')
        return True
    else:
        print('Você perdeu!')
        return False

#Aqui o programa define a função da terceira fase

def fase3(gato,rato,osso):

# Aqui o programa chama a função do mapa da fase

    local = ' ','*','*','*',' ','G',' ','*'
    imprimeMapa(local)

# Aqui o usuário define onde colocará os hóspedes

    gt = int(input(gato))
    rt = int(input(rato))
    int(input(osso))

# Aqui o programa irá conferir se os hóspedes foram colocados nos locais corretos e irá retornar True caso o usuário tenha acertado e False caso tenha errado

    if (rt == 1) and (gt != 5):
        print('Sucesso! Próxima fase desbloqueada!')
        return True
    else:
        print('Você perdeu!')
        return False

#Aqui o programa define a função da quarta fase

def fase4(queijo1,queijo2,osso):

# Aqui o programa chama a função do mapa da fase

    local = ' ',' ',' ','*','*','R','*','*'
    imprimeMapa(local)

# Aqui o usuário define onde colocará os hóspedes

    int(input(queijo1))
    int(input(queijo2))
    os = int(input(osso))

# Aqui o programa irá conferir se os hóspedes foram colocados nos locais corretos e irá retornar True caso o usuário tenha acertado e False caso tenha errado

    if (os != 2):
        print('Você perdeu!')
        return False
    else:
        return True

#Este é o programa principal

#Esta é a tela inicial do do programa

print('HOTEL DOS ANIMAIS')
print('Decida onde cada hóspede deve ficar!')
print('Restrições:')
print('O rato não pode ficar ao lado do gato.\nO cão não pode ficar ao lado do osso.\nO gato não pode ficar ao lado do cão.\nO queijo não pode ficar ao lado do rato')
print('FASE 1')
print('Escolha onde ficarão o Gato e o Rato: ')

#Esta parte do programa chamará as funções e ao final checará se o resultado retornado pela função é True, caso sim, o usuário será levado a próxima fase, caso contrário o programa encerrará.

f1 = fase1('Onde ficará o Rato? ','Onde ficará o Gato? ')
if f1:
    print('FASE 2')
    print('Escolha onde ficarão os dois Cães e o Osso: ')
    f2 = fase2('Onde ficará o primeiro Cão? ','Onde ficará o segundo Cão? ','Onde ficará o Osso? ')
    if f2:
        print('FASE 3')
        print('Escolha onde ficarão o Gato, o Rato e o Osso: ')
        f3 = fase3('Onde ficará o Gato? ', 'Onde ficará o Rato? ', 'Onde ficará o Osso? ')
        if f3:
            print('FASE 4')
            print('Escolha onde ficarão os Queijos e o Osso: ')
            f4 = fase4('Onde ficará o primeiro Queijo? ', 'Onde ficará o segundo Queijo? ', 'Onde ficará o Osso? ')
            if f4:

#Caso o usuário tenha passado efetivamente por todas as fases, ao final do programa receberá a mensagem abaixo

                print('Você ganhou!')