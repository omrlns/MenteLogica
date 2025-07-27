def numeroPrimo(numero):
    if (numero <= 1):
        return False
    for i in range(2, numero):
        if (numero % i == 0):
            return False
    return True

numero = int(input('DIGITE UM NÚMERO PARA SABER SE ELE É PRIMO: '))
if (numeroPrimo(numero)):
    print('{} É UM NÚMERO PRIMO!'.format(numero))
else:
    print('{} NÃO É UM NÚMERO PRIMO!'.format(numero))