'''Desenvolva um programa que leia seis númeor sinteiros e mostre a soma apenas daqueles que são pares.'''

s = 0
count = 0
for c in range(0, 6+1):
    n = int(input('Informe um número: '))
    if n % 2 == 0:
        s += n
        count += 1
print('Dos {} números digitados, apenas {} são pares e a soma deles é {}.'.format(c, count, s))
