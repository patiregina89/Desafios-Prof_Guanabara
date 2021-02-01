'''Escreva um programa para aprovar um emprestimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode ultrapassar 30% do salário ou então o emprestimo será negado.'''

#pedido de informações
valor_casa = float(input('Informe o valor da casa que você pretende comprar: R$ '))
salario = float(input('Informe seu salário atual: R$ '))
tempo_pgto = int(input('Informe em quantos anos gostaria de quitar seu emprétimo: '))

#contas
minimo = salario * 0.30
prestacao_mensal = valor_casa / (tempo_pgto * 12)
print('Para pagar uma casa de {:.2f} em {} anos, o valor da prestação será de R$ {:.2f}.'.format(valor_casa, tempo_pgto, prestacao_mensal))

#programa
if prestacao_mensal <= minimo:
    print('Empréstimo CONCEDIDO!')
else:
    print('Empréstimo NEGADO')



print('Comparando:  a prestação é de {:.2f} e 30% do salário que é: {}'.format(prestacao_mensal, minimo))
