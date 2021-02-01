'''Desenvolva um programa que leia o nome, idade, sexo de 4 pessoas e no final mostre:
a média de idade
qual o nome do homem mais velho
e quantas mulheres tem menos de 20 anos'''

somaidade = 0
media = 0
velho = 0
nomevelho = ''
mulher20 = 0
for pessoa in range(1, 5):
    print('------------{}ª Pessoa------------'.format(pessoa))
    nome = str(input('Nome: '.format(pessoa)))
    idade = int(input('Idade: '.format(pessoa)))
    sexo = str(input('Sexo (F/M): '.format(pessoa)))
    somaidade += idade
    media = somaidade / pessoa
    if pessoa == 1 and sexo in 'Mm':
        velho = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > velho:
        velho = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        mulher20 += 1
print('A média das idades é {}, sendo que homem mais velho tem {} anos e se chama {} e tem {} mulheres com menos de 20 anos.'.format(media, velho, nomevelho, mulher20))
