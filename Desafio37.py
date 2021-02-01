'''Escreva um programa que leia um número inteiro  qualquer e peça para o usuário ecolher a conversão que deseja:
1 para binário
2 para octal
3 para hexadecimal'''

# informações:
num = int(input('Informe um número qualquer: '))

# menu de opções:
print('''Escolha uma das bases para conversão:
1 - binário
2 - octal
3 - hexadecimal''')
opcao = int(input('Sua opção: '))

#programa
if opcao == 1:
    print('{} convertido para binário é {}.'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para octal é {}.'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para hexadecimal é {}.'.format(num, hex(num)[2:]))
else:
    print('Opção inválida!')
