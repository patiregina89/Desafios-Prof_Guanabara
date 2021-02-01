'''Crie um programa que leia uma frase qualquer e diga se ele é palíndrome, desconsiderando os espaços.'''

frase = str(input('Digite uma frase: ')).strip().upper() #.strip tira os espaços vazios e .upper deixa tudo maiúscula.
palavras = frase.split()        #.split divide a frase em palavras
junto = ''.join(palavras)       #.join faz a junção das palavras sem o espaço.
inverso = ''
for letra in range(len(junto) -1, -1, -1): #len separa a palara em letras. entao o programa vai pegar a última letra da variável junto, e correr até o -1. de forma inversa (-1)
    inverso += junto[letra]
if junto == inverso:
    print('É palindromo!', junto, ' >>> ', inverso)
else:
    print('Não é palíndromo', junto, ' >>> ', inverso)
