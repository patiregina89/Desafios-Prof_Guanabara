'''Faça um programa que leia o nome completo de uma pessoa, mpostrando o primeiro e o último nome separadament.'''

nome = str(input('Informe seu nome completo: ')).strip()
n = nome.split()
print('Seu primeiro nome é {} e seu último nome é {}.'.format(n[0], n[len(n)-1]))
