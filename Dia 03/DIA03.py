linha = '--------------------------------------------------'
# OPERADORES E EXPRESSÕES

# 1, calculando o troco
# preços dos itens
pao = 11.98
leite = 4.75
cafe = 21

# total da compra
total_compra = pao + leite + cafe

# valor pago
valor_pago = 50

#calcular troco
troco = valor_pago - total_compra

print('total da compra: R$', round(total_compra, 2)) 
# usamos round() para definir o número de casas depois da vírgula
print('troco a receber: R$', round(troco, 2))   
print(linha)

# 2, verificando aprovação em um exame
# dados do estudante
nota_media = 8.5
frenquenia = 80

#  verificar aprovação
aprovado = (nota_media >= 7.0) and (frenquenia >= 75)
print('estudante aprovado?', aprovado)
print(linha)

# 3, oferta especial
#  dados da compra
quantidade_itens = 8
valor_total = 120

# verificar desconto
desconto = (quantidade_itens > 10) or (valor_total > 100)
print('cliente tem direito ao desconto?', desconto) # True
print(linha)

# 4, sistema de acesso
# dados do usuário
senha_inserida = 'abcd1234'
senha_correta = '1234abcd'
usuario_bloqueado = False

# verificar acesso
acesso_concedido = (senha_inserida == senha_correta) and not usuario_bloqueado
print('acesso concedido?', acesso_concedido)
print(linha)

# 5, dividindo a conta
# valor total da conta
conta = 150

# número de amigos
amigos = 5
valor_por_pessoa = conta / amigos

# verificar se a divisão é exata
divisao_exata = (conta % amigos) == 0
print('cada um deve pagar: R$', valor_por_pessoa)
print('a divisão é exata?', divisao_exata) #True
print(linha)

# DESAFIOS EXTRAS

# 1, classificação etária
# solicitar idade
idade = int(input('informe a sua idade: '))

# verificar permissão
pode_assistir = idade >= 16
print('pode assistir ao filme?', pode_assistir)
print(linha)

# 2, calculadora de IMC
# solicitar peso e altura
peso = float(input('informe o seu peso em kg: '))
altura = float(input(' digite a sua altura em metros: '))

# calcular IMC
imc = peso / (altura ** 2 )

# verificar peso ideal
peso_ideal = (imc >= 18.5) and (imc <= 24.9)
print('seu IMC é:', imc)
print('você está no peso ideal?', peso_ideal)
print(linha)

# 3, par ou impar
# solicitar número
numero = int(input('digite umn número: '))

# verificar se é par ou impar
par = (numero % 2) == 0
print('o número é par?', par)

