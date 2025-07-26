def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividr(a, b):
    return a / b

continuar = 'S'

while True:
    while continuar == 'S':
        print('=' * 50)
        print(f'{'CALCULADORA SIMPLES':^50}')
        print('=' * 50)

        numero1 = int(input('INFORME O PRIMEIRO NÚMERO INTEIRO: '))
        numero2 = int(input('INFORME O SEGUNDO NÚMERO INTEIRO: '))
        print('''
ESCOLHA UMA OPERAÇÃO PARA REALIZAR O CÁLCULO:

[1] ADIÇÃO
[2] SUBTRAÇÃO
[3] MULTIPLICAÇÃO
[4] DIVISÃO
    ''')
        operacao = int(input('INFORME A SUA ESCOLHA: '))
        if (operacao == 1):
            resultado = somar(numero1, numero2)
            print('\nVOCÊ DIGITOU {} E {}. A OPERAÇÃO ESCOLHIDA FOI "ADIÇÃO".'.format(numero1, numero2))
            print('O RESULTADO É: {}'.format(resultado), '\n')
        elif (operacao == 2):
            resultado = subtrair(numero1, numero2)
            print('\nVOCÊ DIGITOU {} E {}. A OPERAÇÃO ESCOLHIDA FOI "SUBTRAÇÃO".'.format(numero1, numero2))
            print('O RESULTADO É: {}'.format(resultado), '\n')
        elif (operacao == 3):
            resultado = multiplicar(numero1, numero2)
            print('\nVOCÊ DIGITOU {} E {}. A OPERAÇÃO ESCOLHIDA FOI "MULTIPLICAÇÃO".'.format(numero1, numero2))
            print('O RESULTADO É: {}'.format(resultado), '\n')
        elif (operacao == 4):
            resultado = dividr(numero1, numero2)
            print('\nVOCÊ DIGITOU {} E {}. A OPERAÇÃO ESCOLHIDA FOI "DIVISÃO".'.format(numero1, numero2))
            print('O RESULTADO É: {}'.format(resultado), '\n')
        else:
            print('OPÇÃO INVÁLIDA! TENTE NOVAMENTE!')
        
        continuar = str(input('VOCÊ DESEJA INFORMAR NOVOS NÚMEROS? [S/N] ')).strip().upper()[0]
        if (continuar != 'S'):
            print('\nENCERRANDO O PROGRAMA...')
            break
            



