'''Faça um prograna que leia um número inteiro e diga se ele é primo ou não'''

n = int(input('Digite um número: '))
total = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[1;34m', end='')
        total += 1
    else:
        print('\033[m', end=' ')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisivel {} vezes.'.format(n, total))
if total == 2:
    print('Por isso ele é primo!')
else:
    print('Por isso ele não é primo')

