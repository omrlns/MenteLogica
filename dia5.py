linha = '--------------------------------------------------'
# ESTRUTURAS DE REPETIÇÃO

# EXERCÍCIOS PRÁTICOS
# 1, imprimindo números de 1 a 10
for numero in range(1, 11):
    print(numero)
# análise, o range(1, 11) gera números de 1 a 10 (ó último valor é excluído)
print(linha)

# 2, calculando a soma dos números de 1 a N
N = int(input('dogote um número inteiro positivo: '))
soma = 0

for i in range(1, N+1):
    soma += i # equivale a soma = soma + i
print (' a soma dos números de 1 a', N, 'é', soma)
print(linha)

# 3, tabuada de um número
numero = int(input('digite um número para ver sua tabuada: '))

for i in range(1, 11):
    resultado = numero * i
    print(f'{numero} x {i} = {resultado}')

print(linha)

# 4, contando números pares e ímpares
pares = 0
impares = 0

for numero in range(1, 21):
    if numero % 2 == 0:
        pares += 1 
    else:
        impares += 1

print('quantidade de números pares:', pares)
print('quantidade de números pares:', impares)
print(linha)

# 5. adivinhe o número
import random

numero_secreto = random.randint(1, 100)
tentativas = 0

while True:
    palpite = int(input('adivinhe o número (entre 1 e 100): '))
    tentativas += 1
# usa um loop while que continua até o usuário acertar.
    if palpite == numero_secreto:
        print(f'parabéns! você acertou em {tentativas} tentativas.')
        break #o break é usado para sair do loop quando o número é adivinhado.
    elif palpite < numero_secreto:
        print("o número é maior.")
    else:
        print('o número é menor.')
print(linha)

# DESAFIOS EXTRAS
# 1, calculando o fatorial de um número
# fatorial de N (N!) é o produto de todos os números positivos de 1 até N.
N = int(input('digite um número inteiro positivo: '))
fatorial = 1

if N < 0:
    print('não existe fatorial de número negativo.')
# sempre lembrar de fazer uma tratativa, porque usuário é usuário.
elif N == 0 or N == 1:
    print(f'o fatorial de {N} é 1.')
else:
    for i in range(1, N+1):
        fatorial *= i
    print(f'o fatorial de {N} é {fatorial}.')
print(linha)

# 2, série fibonacci
# exiba os primeiros N termos da série de fibonacci
# a série de fibonacci começa com 0 e 1, e cada termo subsequente é a soma dos dois anteriores.
# exemplo: 0, 1, 1, 2, 3, 5...
N = int(input('quantos termos da série de fibonacci você quer ver? '))
termo1 = 0
termo2 = 1
contador = 0

if N <= 0:
    print('por favor, insira um número positivo.')
elif N == 1:
    print('série de fibonacci até', N, 'termo:')
    print(termo1)
else:
    print('série fibonacci:')
    while contador < N:
        print(termo1)
        proximo_termo = termo1 + termo2
        termo1 = termo2
        termo2 = proximo_termo
        contador += 1
print(linha)

# 3, joga da forca, simples
palavra_secreta = 'python'
letras_descobertas = ['_'] * len(palavra_secreta)
tentativas = 6

while tentativas > 0 and '_' in letras_descobertas:
    print('palavra:', ' '.join(letras_descobertas))
    letra = input('digite uma letra: ').lower()
    
    if letra in palavra_secreta:
        for idx, letra_secreta in enumerate(palavra_secreta):
            if letra == letra_secreta:
                letras_descobertas[idx] = letra
        print('boa, você acerto uma letra.')
    else:
        tentativas -= 1
        print(f'você errou! você tem {tentativas} tentativas restantes.')

if '_' not in letras_descobertas:
        print('parabéns! você adivinhou a palavra:', palavra_secreta)
else:
        print('você perdeu! a palavra era:', palavra_secreta)