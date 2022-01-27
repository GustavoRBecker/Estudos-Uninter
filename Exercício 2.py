#Esta é a função que irá realizar a troca das vogais
def troca(nome):
    x = input(nome)

#Aqui o algoritmo irá colocar todas as letras como maiúsculas
    x = x.upper()

#Aqui acontecerá a troca das vogais
    x = x.replace('A', '@')
    x = x.replace('E', '&')
    x = x.replace('I', '!')
    x = x.replace('O', '#')
    x = x.replace('U', '*')
    return x

#Este é o programa principal
x = troca('Digite um nome: ')

#Aqui o programa realizará a impressão na tela do nome já convertido
print(x)