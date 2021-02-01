'''Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas
o nome com todas as letras minúsculas
quantidade de letras ao todo (sem espaço)
quantas letras tem o primeiro nome'''

nome = str(input('Informe seu nome: '))
print(nome.upper())
print(nome.lower())
print('Seu nome tem {} letras.'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))