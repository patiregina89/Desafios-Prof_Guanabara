'''Refaça o desfaio 009 mostrando a tabuada de um número que o usuário escolher usando o for:'''

n = int(input('Informe qual tabuada você deseja saber: '))
for c in range(0, 10+1):
    #print(n, 'x', c, ' = ', n*c)
    print('{} x {} = {}'.format(n, c, n*c))
