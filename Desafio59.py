'''Crie um programa que leia dois valores e mostre um menu na tela.
1 - somar
2 - multiplicar
3 - maior
4 - novos números
5 - sair do programa
O programa deverá realizar a operação solicitada em cada caso'''

num1 = int(input('Informe um número: '))
num2 = int(input('Informe outro número: '))
maior = num1
opcao = 0
while opcao != 5:
    print('[1] Somar \n[2] Multiplicar \n[3] Maior \n[4] Novos números \n[5] Sair do programa')
    opcao = int(input('Qual opcão deseja? '))
    if opcao == 1:
        print('{} + {} = {}'.format(num1, num2, num1+num2))
    elif opcao == 2:
        print('{} x {} = {}'.format(num1, num2, num1*num2))
    elif opcao == 3:
        if num2 > maior:
            maior = num2
            print('O número {} é maior.'.format(maior))
        else:
            maior = num1
            print('O número {} é maior.'.format(maior))
    elif opcao == 4:
        num1 = int(input('Informe um número: '))
        num2 = int(input('Informe outro número: '))
    elif opcao == 5:
        break
        print('Você saiu do programa')
    else:
        print('Opcão inválida. tente novamnete.')
print('Fim do programa!')