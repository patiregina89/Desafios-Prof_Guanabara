'''Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício. indo de 10 até 0 com pausa de um segundo'''
from time import sleep
for c in range(10, 0-1, -1):
    print(c)
    sleep(1)
print('Feliz Ano Novo!!')