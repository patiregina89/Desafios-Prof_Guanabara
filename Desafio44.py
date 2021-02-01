'''Elabore um programa que calcule o valor a ser pago em um produto, considerando seu preço normal e condição de pagamento:
à vista dinheiro/cheque: 10% desconto
à vista cartão: 5% desconto
até 2x no cartão: preço normal
3x ou mais no cartão: 20% de juros'''
#informações:
valor_produto = float(input('Informe o valor do produto R$ '))
print('''Formas de pagamento:
[1] à vista no dinheiro ou cheque
[2] à vista do cartão
[3] até 2x no cartão de crédito
[4] 3x ou mais no cartão de crédito''')
opcao = int(input('Informe a opção desejada: '))

#programa
if opcao == 1:
    total = valor_produto - (valor_produto * 0.10)
    print('O produto de R$ {:.2f} para pagamento à vista (dinheiro/cheque) tem 10% de desconto, portanto o valor total a pagar é R$ {:.2f}'.format(valor_produto, total))
elif opcao == 2:
    total = valor_produto - (valor_produto * 0.05)
    print('O produto de R$ {:.2f} para pagamento à vista (cartão) tem 5% de desconto, portanto o valor total a pagar é R$ {:.2f}'.format(valor_produto, total))
elif opcao == 3:
    total = valor_produto
    print('O produto para no cartão em até 2x não tem desconto ou acréscimo, portanto o valor total a pagar é R$ {:.2f}'. format(total))
elif opcao == 4:
    total = valor_produto + (valor_produto * 0.20)
    print('O produto de R$ {:.2f} para pagamento cartão (3x ou mais) tem 20% de juros, portanto o valor total a pagar é R$ {:.2f}'.format(valor_produto, total))
else:
    print('\033[31mOpção INVÁLIDA!')