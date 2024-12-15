linha = '--------------------------------------------------'
#ESTRUTURAS CONDICIONAIS

# 1, decidindo o que vestir
clima = 'chuvoso'

if clima == 'ensolarado':
    print('vista um camiseta e shorts.')
elif clima == 'nublado':
    print('leve uma jaqueta leve.')
elif clima == 'chuvoso':
    print('não esqueça o guarda-chuva.')
else:
    print('verifique a previsão do tempo.')

print(linha)

# 2, semáforo
semaforo = 'vermelho'

if semaforo == 'verde':
    print('siga em frente.')
elif semaforo == 'amarelo':
    print('prepare-se para parar.')
elif semaforo == 'vermelho':
    print('pare o veículo.')
else:
    print('sinal desconhecido, proceda com cautela.')

print(linha)


# 3, calculando descontos em compra
valor_compra = 750

if valor_compra >= 1000:
    desconto = valor_compra * 0.10
    print('você recebeu um desconto de 10%. valor do desconto: R$', desconto)
elif valor_compra >= 500:
    desconto = valor_compra * 0.05
    print('você recebeu um desconto de 5%. valor do desconto: R$', desconto)
else:
    desconto = 0
    print('não há desconto disponível.')

valor_final = valor_compra - desconto
print("valor final da compra: R$", valor_final)
print(linha)

# 4, planejando um passeio
dia_da_semana = 'sábado'

chovendo = False
if (dia_da_semana == 'sábado' or dia_da_semana == 'domingo') and not chovendo:
    print('ótimo dia para ir ao parque!')
else:
    print('vamos ficar em casa e assistir a um filme.')

print(linha)

