'''Faça um programa que leia um ângulo qqr e mostre o na tela o valor de seno, cosseno e tangente desse angulo'''

import math
angulo = float(input('Digite um angulo: '))
seno = math.sin(math.radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))

cos = math.cos(math.radians(angulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cos))

tangente = math.tan(math.radians(angulo))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))