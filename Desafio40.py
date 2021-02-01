'''Crie um programa que leia duas notas de aluno e calcule sua média.
Média abaixo de 5: reprovado
média entre 5 e 6.9: recuperação
média maior que 7: aprovado.'''
#informações:
n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))

#calculos:
media = (n1 + n2) / 2

#programa:
if media < 5:
    print('A média do aluno é {:.2f}, portanto o aluno está REPROVADO!'.format(media))
elif 7 < media >= 5:
    print('A média do aluno é {:.2f}, portanto o aluno está em RECUPERAÇÃO!'.format(media))
elif media >= 7:
    print('A média do alino é {:.2f}, portanto o aluno está APROVADO!'.format(media))
