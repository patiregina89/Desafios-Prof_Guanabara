'''Crie um programa que leia o nome deuma pessoa e diga se ela tem SILVA no nome'''

nome = str(input('Informe seu nome completo?  ')).strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))