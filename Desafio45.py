'''Crie um programa que faça o computador jogar jokenpô com você'''

from random import randint
from time import sleep

itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)

#informação:
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!')
print()
print('O computador escolheu {}'.format(itens[computador]))
print('O jogador escolheu {}'.format(itens[jogador]))


#programa
if computador == 0: #pedra
    if jogador == 0:
        print('\033[33mEmpate!')
    elif jogador == 1:
        print('\033[32mJogador VENCEU!')
    elif jogador ==2:
        print('\033[34mJogador PERDEU!')
    else:
        print('\33[41mJogada Inválida!')
if computador == 1: #papel
    if jogador == 0:
        print('\033[34mJogador PERDEU!')
    elif jogador == 1:
        print('\033[33mEmpate!')
    elif jogador == 2:
        print('\033[32mJogador VENCEU!')
    else:
        print('\033[41mJogada Inválida!')
if computador == 2: #tesoura
    if jogador == 0:
        print('\033[32mJogador VENCEU!')
    elif jogador == 1:
        print('\033[34mJogador PERDEU!')
    elif jogador == 2:
        print('\033[33mEmpate!')
    else:
        print('\033[41mJogada Inválida!')


#OBS: O PROGRAMA ESTÁ COM ERRO. SE JOGAR ALGUM NÚMERO QUE NÃO PERTENCE A LISTA DÁ ERRO.