'''Crie um programa que mostre na tela todos os números pares que estão no intervalo de 1 e 50'''


'''for c in range(1, 50+1):
    if c % 2 == 0:
        print(c)'''


# pode ser feito das 2 formas, sendo a de baixo o programa "trabalha"menos e fica mais leve.


for c in range(2, 50+1, 2):
    print(c)