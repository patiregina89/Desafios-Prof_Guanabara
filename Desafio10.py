#crie um programd e quanto dinheiro a pessoa tem na carteira e mostre quantos dolares pode comprar (US$1 = R$3,27)
real = float(input('Informe quantos reais você possui: '))
dolar = real // 3.27
valorexato = 3.27*dolar
print('Você pode adquirir {:.0f} dólares com {:.0f} reais'.format(dolar, valorexato))