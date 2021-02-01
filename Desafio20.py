'''O mesmo professor do exercício anterior, quer sortear a ordem de apresentação dos trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mosre a ordem sorteada.'''

'''import random
aluno1 = str(input('Informe o nome do primeiro aluno: '))
aluno2 = str(input('Informe o nome do segundo aluno: '))
aluno3 = str(input('Informe o nome do terceiro aluno: '))
aluno4 = str(input('Informe o nome do quarto aluno: '))
sorteio = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(sorteio)
print('A ordem de apresentação será: ')
print(sorteio)'''


from random import shuffle
aluno1 = str(input('Informe o nome do primeiro aluno: '))
aluno2 = str(input('Informe o nome do segundo aluno: '))
aluno3 = str(input('Informe o nome do terceiro aluno: '))
aluno4 = str(input('Informe o nome do quarto aluno: '))
sorteio = [aluno1, aluno2, aluno3, aluno4]
shuffle(sorteio)
print('A ordem de apresentação será: ')
print(sorteio)