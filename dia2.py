# declarando variáveis
nome = 'Marlon'
idade = 21
altura = 1.77
estudante = True
linha = '--------------------------------------------------'

# exibindo informações
print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('Estudante:', estudante)
print(linha)

# operações simples
ano_nascimento = 2024 - idade
print('Ano de Nascimento:', ano_nascimento)
print(linha)

maior_de_idade = idade >= 18
print('Maior de idade:', maior_de_idade)
print(linha)

# manipulação de strings
frase = 'Olá, meu nome é ' + nome + ' e eu tenho ' + str(idade) + ' anos.'
print(frase)
print(linha)

# calculadora simples
numero1 = float(input('digite o primeiro número: '))
numero2 = float(input('digite o segundo número: '))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2

print('Os números digitados foram: ' + str(numero1) + ' e ' + str(numero2))
print((linha))
print('O resultado da soma dos dois números é:', soma)
print('O resultado da subtração dos dois números é:', subtracao)
print('O resultado da multiplicação dos dois números é:', multiplicacao)
print('O resultado da divisão dos dois números é:', divisao)
print(linha)

# conversor de temperaturas
# fórmula: F = C * 9/5 + 32

celsius = float(input('digite a temperatura em Celsius: '))
fahrenheit = celsius * 9/5 + 32
print('a temperatura em Fahrenheit é:', fahrenheit)
print(linha)

# calculando a Área de um círculo
# fórmula: Área = π * raio² 
# use π = 3.14159

raio = float(input('digite o raio do círculo: '))
pi = 3.14159
area = pi * raio ** 2
print('a área do círculo é:', area) 