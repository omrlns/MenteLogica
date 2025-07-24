def teste():
    pass # palavra-chave usada como placeholder para quando não haver código dentro da função

def saudacao():
    print('hello world!')

saudacao() # vai retornar 'hello world!'

def soma(a, b):
    resultado = a + b
    return resultado # se não tivesse o return, o valor iria ficar por somente dentro da função

total = soma(5, 5)
print('O resultado da operação é: {}'.format(total))


