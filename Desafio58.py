'''Melhore o jogo do desafio 28. O computador vai pensar em um número de 0 a 10 e o jogador vai tentar adivinhar até acertar.
No final mostra quantos palpites foram necessários para vencer.'''

from random import randint
computador = randint(0,10)
print('Pensei em um número de 0 a 10. Tente adivinhar qual foi!')
acertou = False
palpite = 0

while not acertou:
    jogador = int(input('Qual número eu pensei? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente novamente.')
        elif jogador > computador:
            print('Menos.. tente novamente.')
print('Parabéns, você acertou!')
print('Você precisou {} palpites para acertar.'.format(palpite))
