'''Desenvolva  um programa que leia o primeiro termo e a razão de um PA. No final mostre os 10 primeiros termos dessa progressão.'''


pt = int(input('Informe o primeiro termo: '))
r = int(input('Informe a razão: '))
dec = pt + (10 - 1) * r
for c in range(pt, dec + r, r):
    print('{}'.format(c), end=' ► ')
print('Fim!')