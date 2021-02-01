'''Faça um programa que leia o ano de nascimento e informe conforme sua idade:
- Se ele vai se alistar no programa militar
- Se é a hora de se alistar no programa militar
- Se já passou do tempo do alistamento
O programa deverá mostrar o tempo que falta ou passou para o alistamento'''
#Ppara saber qual ano estamos:
from datetime import date
atual = date.today().year
#informação:
nascimento = int(input('Informe o ano que nasceu: '))

#calculos:
idade = atual - nascimento

#programa:
if idade == 18:
    print('você deve se alistar esse ano!')
elif idade < 18:
    prazo = 18 - idade
    print('Ainda não chegou sua hora. Falatam {} anos para seu alistamento'.format(prazo))
elif idade > 18:
    prazo = idade - 18
    print('Você deveria ter se alistado {} anos atras'.format(prazo))
