# jogo de adivinhação

# o computador escolhe um número aleatório entre 1 e 100.
# o jogador tem um número limitado de tentativas para adivinhar o número.
# a cada palpite, o programa fornece dicas, informando se o número é maior ou menor.
# o jogador acumula pontos com base no número de tentativas.
# o jogo armazena as pontuações em uma lista e exibe o placar ao final.

from random import randint

# lista para armazenar as pontuações
pontuacao = []
tentativasRestantes = 10

print('CPU: EU PENSEI EM UM NÚMERO DE 1 A 100, VOCÊ CONSEGUE ADIVINHAR?')
while tentativasRestantes >= 1:
    numeroCPU = randint(1, 10)
    palpite = int(input('INFORME O SEU PALPITE: '))
    if (palpite < 1 or palpite > 100):
        print('ERRO! DIGITE UM NÚMERO DE 1 A 100.')
    if (palpite == numeroCPU):
        print('VOCÊ ACERTOU!')
        pontuacao.append(tentativasRestantes * 5)
        break
print()
print('PONTUAÇÃO: {} ponto(s)!'.format(pontuacao))
