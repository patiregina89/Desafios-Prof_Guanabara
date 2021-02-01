#faça um programa que leia a altura e largura da parede e calcule sua área e a quantidade de tinta. Sabendo que cada litro de tinta pinta 2m²
altura = float(input('Informe a altura da parede: '))
largura = float(input('Informe a largura da parede: '))
areat = altura * largura
qtdtinta = areat/2
print('A área total da sua parede é de {}m². Portanto você irá precisar de {} litros de tinta para pintar sua parede'.format(areat, qtdtinta))