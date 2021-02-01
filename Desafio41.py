'''A confedereção Nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria:
- até 9 anos: mirim
- até 14 anos: infantil
- até 19 anos: junior
- ate 20 anos: sênior
- acima: master'''
from datetime import date
ano_atual = date.today().year

#informações
nasc = int(input('Informe o ano de nascimento:'))

#calculo:
idade = ano_atual - nasc

#programa:
if idade <= 9:
    print('O atleta de {} anos competirá na categoria MIRIM.'.format(idade))
elif 9 < idade <= 14:
    print('O atleta de {} anos competirá na categoria INFANTIL.'.format(idade))
elif 14 < idade <= 19:
    print('O atelate de {} anos conpetirá na categoria JUNIOR.'.format(idade))
elif 19 < idade <= 20:
    print('O atleta de {} anos competirá na categoria SÊNIOR.'.format(idade))
elif idade > 20:
    print('O atleta de {} anos competirá na categoria MASTER.'.format(idade))
