#faça um algorítimo que lei o salário d eum funcionário e motre seu novo salário com um aumento de 15%.
salario = float(input('Informe seu salário atual: '))
aumento = salario + (salario*0.15)
print('Informamos que a partir de agora, você teve um aumento de 15% e seu salário passará a valer R$ {:.2f}'.format(aumento))