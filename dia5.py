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




