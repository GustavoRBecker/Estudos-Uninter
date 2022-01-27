km = int(input('Digite quantos km você percorreu com o veículo: '))
dias = int(input('Digite quantos dias você ficou com o veículo: '))

preco = km * 0.15 + dias * 60

print('Você rodou {} km com o veículo durante o período de {} dias, portanto terá de pagar o valor de {}.'.format(km,
                                                                                                                  dias,
                                                                                                                  preco))

frase = input('Digite uma frase qualquer: ')
tam = len(frase)

frase2 = frase[:int(tam / 2)]
print(frase2[-2:])
