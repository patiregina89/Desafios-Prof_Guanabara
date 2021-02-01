'''Faça um programa que leia o sexo de uma pessoa, mas só aceite M ou F. Caso digite errado de uma msg de erro e repita a pergunta até acertar.'''

sexo = str(input('Informe o sexo [M/F]: ')).upper()[0].strip()
while sexo not in 'MF':
    sexo = str(input('Dados inválidos! Por favor informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))
