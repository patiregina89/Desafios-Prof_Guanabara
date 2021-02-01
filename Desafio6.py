#crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrda.
n = int(input('Informe um número: '))
d = n * 2
t = n * 3
r = n ** 1/2
print('O número informado é {}. Seu dobro é {}, o triplo é {} e raiz quadrada é {:.0f}'.format(n, d, t, r))
