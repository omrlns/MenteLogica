linha = '--------------------------------------------------'
# ESTRUTURAS CONDICIONAIS

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

# EXERCÍCIOS PRÁTICOS
# 1, verificando se um número é positovo, negativo ou zero
numero = float(input('digite um número: '))

if numero > 0:
    print('o número é positivo.')
elif numero < 0:
    print('o número é negativo.')
else:
    print('o número é zero.')

print(linha)

# 2, calculadora simples
numero1 = float(input('digite o primeiro número: '))
numero2 = float(input('digite o segundo número: '))
operacao = input('digite a operação (+, -, *, /): ')

if operacao == '+':
        resultado = numero1 + numero2
        print('resultado:', resultado)
elif operacao == '-':
        resultado = numero1 - numero2
        print('resultado:', resultado)
elif operacao == '*':
        resultado = numero1 * numero2
        print('resultado:', resultado)
elif operacao == '/':
    if numero2 != 0:
        resultado = numero1 / numero2
        print('resultado:', resultado)
    else:
        print('erro: divisão por zero!')
else:
     print('operação inválida.')

print(linha)

# 3, classificação de idade
idade = int(input('digite a sua idade: '))

if idade >= 0 and idade <= 12:
     print("você é uma criança.")
elif idade >= 13 and idade <= 17:
     print("você é um adolescente.")
elif idade >= 18 and idade <= 59:
     print('você é um adulto.')
elif idade >= 60:
     print('você é um idoso.')
else:
     print('idade inválida.')

print(linha)

# 4, verificando ano bissexto
ano = int(input('digite um ano: '))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 ==0):
     print(ano, 'é um ano bissexto.')
else:
     print(ano, 'não é um ano bissexto.')

print(linha)

# 5, simulador de caixa eletrônico
valor_saque = int(input("digite o valor do saque: R$"))
if valor_saque <= 0:
    print("valor inválido.")
else:
    cedulas_100 = valor_saque // 100
    valor_saque %= 100 #atualiza o valor restante do módulo para as outros notas
    cedulas_50 = valor_saque // 50
    valor_saque %= 50
    cedulas_20 = valor_saque // 20
    valor_saque %= 20
    cedulas_10 = valor_saque // 10
    valor_saque %= 10
    cedulas_5 = valor_saque // 5
    valor_saque %= 5
    cedulas_2 = valor_saque // 2
    valor_saque %= 2
    if valor_saque != 0:
        print("não é possível sacar o valor especificado com as cédulas disponíveis.")
    else:
        print('cédulas entregues:')
        if cedulas_100 > 0:
            print(f"{cedulas_100} x R$100")
        if cedulas_50 > 0:
            print(f"{cedulas_50} x R$50")
        if cedulas_20 > 0:
            print(f"{cedulas_20} x R$20")
        if cedulas_10 > 0:
            print(f"{cedulas_10} x R$10")
        if cedulas_5 > 0:
            print(f"{cedulas_5} x R$5")
        if cedulas_2 > 0:
            print(f"{cedulas_2} x R$2")

# DESAFIOS EXTRAS
# 1, aprovando empréstimo bancário
valor_emprestimo = float(input('digite o valor do empréstimo: R$'))
renda_mensal = float(input('digite a sua renda mensal: R$'))
numero_parcelas = int(input('digite o número de parcelas: '))

valor_parcela = valor_emprestimo / numero_parcelas
limite_parcela = renda_mensal * 0.30

if valor_parcela <= limite_parcela:
     print('empréstimo aprovado.')
     print(f'valor da parcela: R${valor_parcela:.2f}')

else:
     print('empréstimo negado.')
     print(f'valor da parcela R${valor_parcela:.2f} excede 30% da sua renda mensal.')

# 2, jogo do pedra, papel e tesoura
import random

opcoes = ['pedra', 'papel', 'tesoura']

usuario = input('escolha pedra, papel ou tesoura: ').lower()
computador = random.choice(opcoes)

print(f'você escolheu: {usuario}')
print(f'o computador escolheu: {computador}')

if usuario == computador:
     print('empate!')

elif (usuario == 'pedra' and computador == 'tesoura') or \
     (usuario == 'papel' and computador == 'pedra') or \
     (usuario == 'tesoura' and computador == 'papel'): 
    print('você venceu!')
elif usuario in opcoes:
    print('você perdeu!')
else:
     print('escolha inválida.')


print(linha)

# 3, calculadora de tarifas de táxi
distancia = float(input('digite a distância percorrida em km: '))

tarifa_basica = 4.00
custo_por_km = 0.25

valor_total = tarifa_basica + (custo_por_km * distancia)

print(f'valor total da corrida: R${valor_total:.2f}')
print(linha)
