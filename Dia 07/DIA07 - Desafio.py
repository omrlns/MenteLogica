# jogo de adivinhação

# o computador escolhe um número aleatório entre 1 e 100.
# o jogador tem um número limitado de tentativas para adivinhar o número.
# a cada palpite, o programa fornece dicas, informando se o número é maior ou menor.
# o jogador acumula pontos com base no número de tentativas.
# o jogo armazena as pontuações em uma lista e exibe o placar ao final.

from random import randint

# lista para armazenar as pontuações
pontuacoes = []

print('=' * 22)
print(' < GUESS THE NUMBER > ')
print('=' * 22)

while True:
    numeroCPU = randint(1, 100)
    tentativasRestantes = 5
    tentativas = 0

    print('EU PENSEI EM UM NÚMERO ENTRE 1 E 100...')
    print('VOCÊ CONSEGUE ADIVINHAR?')
    print('USE AS SUAS 7 TENTATIVAS SABIAMENTE!')


    while tentativasRestantes > 0:
        palpite = int(input('\nDIGITE O SEU PALPITE: '))

        tentativas += 1
        tentativasRestantes -= 1

        if (palpite == numeroCPU):
            print('PARABÉNS, VOCÊ ACERTOU!')
            print('VOCÊ ACERTOU O NÚMERO EM {} TENTATIVA(S)!'.format(tentativas))
            pontuacao = tentativasRestantes * 10
            pontuacoes.append(pontuacao)
            print('\nSUA PONTUAÇÃO NESTA PARTIDA: {} PONTOS!'.format(pontuacao))
            break
        elif (palpite < numeroCPU):
            print('\nO NÚMERO SECRETO É MAIOR QUE O SEU PALPITE!')
        else:
            print('\nO NÚMERO SECRETO É MENOR QUE O SEU PALPITE!')

        print('\nTENTATIVAS RESTANTES: {}'.format(tentativasRestantes))

    else:
        print('\nQUE PENA, VOCÊ PERDEU! \nO NÚMERO SECRETO ERA: {}'.format(numeroCPU))
        pontuacoes.append(0)

    print('\n < PLACAR > ')
    for i, pontos in enumerate(pontuacoes, start=1):
        print('\nPARTIDA #{}: {} PONTO(S).'.format(i, pontos))

    continuar = input('\nVOCÊ DESEJA JOGAR NOVAMENTE? [S/N] ').strip().upper()[0]
    if (continuar != 'S'):
        print('OBRIGADO POR JOGAR! ATÉ A PRÓXIMA!')
        break

