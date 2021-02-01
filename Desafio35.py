'''Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuário se elas podem ou não formar um triangulo'''

reta1 = float(input('Informe o valor da primeira reta: '))
reta2 = float(input('Informe o valor da segunda reta: '))
reta3 = float(input('Informe o valor da terceira reta: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Os valores informados formam um triângulo!')
else:
    print('Com os valores informados não é possível formar retângulos')