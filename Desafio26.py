'''Faça um programa que leia uma frase pelo teclado e mostre:
qunatas vezes aparece a letra a
em que posição ela aparece pela 1 vez
em queposição ela aperece pela última vez.'''

frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra "a" aparece {} vezes na frase informada'.format(frase.count('A')))
print('A letra "a" aparece pela primeira vez na posição {}.'.format(frase.find('A')+1))
print('A letra "a" aparece pela última vez na posição {}.'.format(frase.rfind('A')+1))