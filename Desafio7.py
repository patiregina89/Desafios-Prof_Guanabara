#desenvolva um programa que leia 2 notas do aluno e calcule e mmostre sua média
n1 = float(input('Informe sua nota 1: '))
n2 = float(input('Informe sua nota 2: '))
media = (n1 + n2)/2
print('A primeira nota informada é {:.2f}, a segunda é {:.2f}, portanto sua média é {:.2f}'.format(n1, n2, media))