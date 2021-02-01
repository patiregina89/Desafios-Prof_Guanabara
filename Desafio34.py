'''escreva um programa que pergunte o salário de um funcionário e calcule o valor de aumento.
Para salários > 1.250 aumento de 10%
Para saláarios < 1.250 aumento de 15%'''

salario = float(input('Favor informar o salário: '))
if salario > 1250:
    aumento = (salario * 0.10) + salario
else:
    aumento = (salario * 0.15) + salario
print('Você recebeu 10% de aumento. O seu salário passa a ser de R${:.2f}'.format(aumento))