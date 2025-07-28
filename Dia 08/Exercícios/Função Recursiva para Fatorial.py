def fatorial(numero):
    if (numero == 0 or numero == 1):
        return 1
    else:
        return numero * fatorial(numero - 1)


numero = int(input('digite um número inteiro positivo: '))
if (numero >= 0):
    resultado = fatorial(numero)
    print('o fatorial de {}! é {}'.format(numero, resultado))
else:
    print('número inválido.')
