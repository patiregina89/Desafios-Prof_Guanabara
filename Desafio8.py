#escreva um programa que leia o valor em metros e exiba convertido em centímetro e milímetros.
m = float (input('Informe o tamanho em metros: '))
cm = m * 100
mm = m * 1000
print('{} metros = {} centrimetros = {} milimetros'.format(m, cm, mm))