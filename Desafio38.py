'''Escreva um programa que leia dois números inteiros e compere-os, mostrando uma msg na tela.
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os 2 são iguais.'''

#informações:
num1 = int(input('Informe o primeiro valor: '))
num2 = int(input('Indorme o segundo valor: '))

#programa:
if num1 > num2:
    print('O PRIMEIRO número digitado é maior.')
elif num2 > num1:
    print('O SEGUNDO número digitado é maior')
else:
    print('Os dois números são IGUAIS.')

# a mesma formula acontece se usar outro elif:
'''elif num1 == num2
    print('Os dois números são IGUAIS)'''
