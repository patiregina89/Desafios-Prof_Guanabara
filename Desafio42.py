'''Refaça o desafio dos triangulos acrescentando o recurso mostrar que tipo de triangulo se formará:
- equilátero: todos os lados iguais
- isósceles: dois lados iguais
- escaleno: todos os lados diferentes'''
#informações:
reta1 = int(input('Informe o valor da primeira reta: '))
reta2 = int(input('Informe o valor da segunda reta: '))
reta3 = int(input('Informe o valor da terceira reta: '))

#programa
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Os valores informados formam um triângulo ', end='')
    if reta1 == reta2 == reta3:
        print('EQUILÁTERO!')
    elif reta1 != reta2 != reta3 != reta1:
        print('ESCALENO!')
    else:
        print('ISÓCELES!')
else:
    print('Com os valores informados não é possível formar retângulos')