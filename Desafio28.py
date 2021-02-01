'''Escrevam um programa que faça o computador pensar em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual o número escolhido,.
o programa deverá escrever na tela se o usuário acertou ou errou.'''

from random import randint
computador = randint(0,5)
#print('Pensei em {}'.format(computador)) -->>> o computador escolhe o número
print('Pensei em número entre 0 e 5, adivinhe qual.')
numerojogador = int(input('Em que número eu pensei? '))
if numerojogador == computador:
    print('Você acertou!!')
else:
    print('Você errou.')