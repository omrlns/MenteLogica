linha = '--------------------------------------------------'
# EXERCÍCIOS PRÁTICOS
# 1, lista de convidados
# cria uma lista com nomes de convidadados para uma festa.
# exiba uma mensagem personalizada para cada convidado.
convidados = ['Ana', 'Bruno', 'Carlos', 'Diana']

for convidado in convidados:
    print(f'Olá, {convidado}! Você está convidado para a festa.')
    print(linha)

# saída:
    # Olá, Ana! Você está convidado para a festa.
    # Olá, Bruno! Você está convidado para a festa.
    # Olá, Carlos! Você está convidado para a festa.
    # Olá, Diana! Você está convidado para a festa.

# 2, estatísticas de números
# peça ao usuário para inserir uma lista de números (separados por espaço) e calcule:
# a) o maior número, b) o menor número, c) a soma dos números, d) a média dos números
entrada = input('digite númeeros separados por espaço: ')
numeros = [float(num) for num in entrada.split()]

maior_numero = max(numeros)
menor_numero = min(numeros)
soma_numeros = sum(numeros)
media_numeros = soma_numeros / len(numeros)

print("maior número:", maior_numero)
print("menor número:", menor_numero)
print("soma dos números:", soma_numeros)
print("média dos números:", media_numeros)
print(linha)

# 3, contagem de caracteres em uma string
# peça ao usuário para inserir uma frase e conte quantas vezes cada letra aparece
frase = input("digite uma frase: ").lower()
letras = {}

for caractere in frase:
    if caractere.isalpha():
        if caractere in letras:
            letras[caractere] += 1
        else:
            letras[caractere] = 1
            
for letra, contagem in letras.items():
    print(f"a letra '{letra}' aparece {contagem} vez(es).")
    print(linha)
    
# saída: o programa vai separar separar as letras da frase e mostrar quantas vezes elas aparecem

# 4, ordenando uma lista
# peça ao usuário para inserir uma lista de números,
# (separados por espaço) e exiba a lista em ordem crescente e decrescente.
entrada = input("digite números separados por espaço: ")
numeros = [float(num) for num in entrada.split()]

# ordem crescente
numeros_crescente = sorted(numeros)
print("números em ordem crescente:", numeros_crescente)

# ordem decrescente
numeros_decrescente = sorted(numeros, reverse = True)
print("números em ordem decrescente:", numeros_decrescente)
print(linha)

# 5, trabalhando com tuplas
# crie uma tupla com nomes de meses do ano. 
# peça ao usuário um número entre 1 e 12 e exiba o nome do mês correspondente.
meses = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")

numero_mes = int(input("Digite um número entre 1 e 12: "))

if 1 <= numero_mes <= 12:
    print(f"o mês correspondente é {meses[numero_mes - 1]}.")
else:
    print("número inválido. Por favor, digite um número entre 1 e 12.")
    print(linha)


