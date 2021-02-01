'''Faça um programa que leia um número e mostre qual seu fatorial.'''

num = int(input('Informe um número: '))
c = num
fatorial = 1
while c > 0:
    print(' {} '.format(c), end='')
    print(' X ' if c > 1 else ' = ', end='')
    fatorial *= c
    c -= 1
print('\n{}! é {}'.format(num, fatorial))
