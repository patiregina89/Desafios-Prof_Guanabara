''' Crie um programa que leia o ano de nascimento de 7 pessoas. No final mostre quantas pessoas ainda sao menores de idade e qunatas são maiores.'''

from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0
for pessoas in range (1, 8):
    nasc = int(input('Qual ano você nasceu? '))
    idade = atual - nasc
    if idade >= 18:
        totalmaior += 1
    else:
        totalmenor += 1
print('{} pessoas são maiores de idade e {} pessoas são menores de idade.'.format(totalmaior, totalmenor))