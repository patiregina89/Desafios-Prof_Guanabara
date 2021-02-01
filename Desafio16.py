'''Crie um programa que leia um número real qualquer pelo teclado e mostre na tela sua porção inteira'''
import math
num = float(input('Digite um número:'))
print('A porção inteira do número {} é {}'.format(num, math.trunc(num)))