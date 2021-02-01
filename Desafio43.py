'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa e calcule o IMC:
abaixo de 18.5: abaixo do peso
18.5 até 25: peso ideal
25 até 30: sobrepeso
30 até 40: obesidade
+ 40: obesidade mórbida'''
#informações:
altura = float(input('Informe sua altura: '))
peso = float(input('Informe seu peso: '))

#calculo:
IMC = peso / (altura ** 2)

#programa:
if IMC <= 18.5:
    print('O IMC é {:.2f}, portanto a pessoa está abaixo do peso ideal.'.format(IMC))
elif 18.5 < IMC <= 25:
    print('O IMC é {:.2f}, portanto a pessoa está com peso ideal.'.format(IMC))
elif 25 < IMC <= 30:
    print('O IMC é de {:.2f}, portanto a pessoa está com sobrepeso.'.format(IMC))
elif 30 < IMC <= 40:
    print('O IMC é {:.2f}, portanto a pessoa está com obesidade.'.format(IMC))
elif IMC > 40:
    print('O IMC é {:.2f}, portanto a pessoa está com obesidade mórbida'.format(IMC))
