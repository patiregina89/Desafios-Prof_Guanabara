'''Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que que ajude ele, lendo o nome deles e mostre o nome escolhido.'''

'''import random
aluno1 = str(input('Informe nome do primeiro aluno: '))
aluno2 = str(input('Informe o nome do segundo aluno: '))
aluno3 = str(input('Informe o nome do terceiro aluno: '))
aluno4 = str(input('Informe o nome do quarto aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]

escolhido = random.choice(lista)
print('O aluno escolhido foi: {}'.format(escolhido))'''

from random import choice
aluno1 = str(input('Informe nome do primeiro aluno: '))
aluno2 = str(input('Informe o nome do segundo aluno: '))
aluno3 = str(input('Informe o nome do terceiro aluno: '))
aluno4 = str(input('Informe o nome do quarto aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]

escolhido = choice(lista)
print('O aluno escolhido foi: {}'.format(escolhido))