'''Faça um programa que calcule a soma entre todos os números ímpares que são multiplos de três num intervalo de 1 - 500'''

s = 0 #a variável S está fazendo um papel de ACUMULADOR, isto é, soma de valores
cont = 0 #a variável cont está fazendo o papel de CONTADOR, isto é, ele soma o item e NÃO seu valor.
for c in range(1, 500+1):
    if c % 3 == 0 and c % 2 == 1:
        cont += 1 #CONTADOR, toda vez que o programa passar pelo contador, ele add mais 1
        s += c #ACUMULADOR do tem valor x e soma + outro valor + outro valor + outro valor...
        print(c)
print('A soma de \033[1;34m{}\033[m valores ímpares divisíveis por 3, no intrevalo de 1-500 é: \033[1;34m{}'.format(cont, s))