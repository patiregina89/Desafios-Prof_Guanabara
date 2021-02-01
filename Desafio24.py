'''Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com nome de santo.'''

cidade = str(input('Digite o nome de uma cidade: ')).strip() #.strip() elimina os espaços em branco
print(cidade[0:5].upper() == 'SANTO')
