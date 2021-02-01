'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar de 80Km/h, mostre uma msg dizendo que foi multado.
A multa vai custar R$ 7,00 por Km acima do limite de velocidade.'''

vel_carro = int(input('Informe a velocidade do carro: '))
if vel_carro > 80:
    limite_excedido = vel_carro - 80
    multa = limite_excedido * 7
    print('Você passou {}km da velocidade permitida. O valor da sua multa é de R$ {:.2f}'.format(limite_excedido, multa))
print('Dirija com segurança!')