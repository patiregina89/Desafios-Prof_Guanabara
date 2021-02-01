'''Desenvolva um programa que pergunte a distância de uma viagem em Km , calcule o preço da passagem:
R$ 0,50 por Km até 200km e R$ 0,45 por Km + de 200)'''

distância = float(input('Informe a distância da sua viagem: '))
if distância <= 200:
    passagem = distância * 0.50
    print('Para uma viagem de {}Km, o preço da passagem é de R$ {:.2f}'.format(distância, passagem))
else:
    passagem = distância * 0.45
    print('Para uma distância de {}Km, o valor da passagem é de R$ {:.2f}'.format(distância, passagem))