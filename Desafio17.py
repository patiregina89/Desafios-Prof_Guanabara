'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo e mostre o comprimento da hipotenusa'''

'''cateto_oposto = float(input('Infome o número do cateto oposto: '))
cateto_adjacente = float(input('Informe o número do cateto adjacente: '))
hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2)
print('A hipotenusa do cateto oposto ({:.0f}) e cateto adjacente ({:.0f}) é: {:.2f}'.format(cateto_oposto, cateto_adjacente, hipotenusa))'''

import math
cateto_oposto = float(input('Infome o número do cateto oposto: '))
cateto_adjacente = float(input('Informeo número do cateto adjacente: '))
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))