#faça um algoritimo que leia o preço do produto e mostre o seu novo preço. com 5% de desconto
p = float(input('Informe o preço do produto: '))
desconto = p - (p * (5/100))
print('O produto está con 5% de desconto, portanto seu valor é de {}'.format(desconto))