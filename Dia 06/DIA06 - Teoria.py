# LISTAS E TUPLAS

# 1, LISTAS
# criando uma lista
frutas = ['maçã', 'banana', 'laranja']

# acessando itens da lista
print(frutas[0]) #saída: maçã
print(frutas[1]) # saída: banana

# modificando itens da lista
frutas[1] = 'morango'
print(frutas) # saída: ['maçã', 'morango', 'laranja']

# adicionando itens na lista
# append(): adiciona um item ao final da lista
frutas.append('uva')
print(frutas) # saída: ['maçã', 'morango', 'laranja', 'uva']

# insert(): insere um item em uma posição específica
frutas.insert(1, 'abacaxi')
print(frutas) # saída: ['maçã', 'abacaxi', 'morango', 'laranja', 'uva']

# removendo itens
# remove(): remove o primeiro item com o valor especificado
frutas.remove('laranja')
print(frutas) # saída: ['maçã', 'abacaxi', 'morango', 'uva']

# pop(): remove o item na posição especificada (ou o último item se nenhum índice for fornecido).
frutas.pop(2)
print(frutas) # saída: ['maçã', 'abacaxi', 'uva']

# comprimendo da lista
# usamos a função len() para obter o número de itens na lista
print(len(frutas)) # saída: 3

# verificando a presença de um item
if 'maçã' in frutas:
    print('maçã está na lista.')

# 2, TUPLAS
# criando uma tupla
cores = ('vermelho', 'azul', 'verde')

# acessando itens da tupla
print(cores[1]) # saída: azul

# tentando modificar uma tupla
# isso resultará em um erro, pois tuplas são imutáveis
# cores[1] = 'amarelo'

# tuplas = + segurança, + perfomance

# convertendo entre listas e tuplas
# lista para tupla
lista_frutas = ['maçã', 'banana', 'laranja']
tupla_frutas = tuple(lista_frutas)
print(tupla_frutas) # saída: ('maçã', 'banana', 'laranja')

# tupla para lista
lista_cores = list(cores)
print(lista_cores) # saída: ['vermelho', 'azul', 'verde']

# ITERAÇÃO SOBRE COLEÇÕES
# iterando sobre listas
frutas = ['maçã', 'banana', 'laranja']

for fruta in frutas:
    print('eu gosto de', fruta)

# saída: 
    # eu gosto de maçã
    # eu gosto de banana
    # eu gosto de laranja

# usando índices
for i in range(len(frutas)):
    print(f'fruta na posição {i}: {frutas[i]}')

# saída:
    # fruta na posição 0: maçã
    # fruta na posição 1: banana
    # fruta na posição 2: laranja

# iterando sobre tuplas
cores = ('vermelho', 'azul', 'verde')

for cor in cores:
    print('a cor é', cor)

# saída:
    # a cor é vermelho
    # a cor é azul
    # a cor é verede

# enumerando itens
# a função enumerate()  permite obeter o índice e o valor ao mesmo tempo
frutas = ['maçã', 'banana', 'laranja']

for indice, fruta in enumerate(frutas):
    print(f'fruta {indice}: {fruta}')

# saída:
    # fruta 0: maçã
    # fruta 1: banana
    # fruta 2: laranja

