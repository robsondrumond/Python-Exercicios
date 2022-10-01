#Exercício 37 (Recebe a entrada de um valor, escolhe a conversão entre binário, octal e hexadecimal)
n = int(input('Digite um número inteiro: '))
opcao = int(input('''Escolha uma das bases para conversão:
[ 1 ] - converter para BINÁRIO
[ 2 ] - converter para OCTAL
[ 3 ] - converter para HEXADECIMAL'''))

if opcao == 1:
    print('{} convertido em binário é {}.' .format(n, bin(n)[2:]))
elif opcao == 2:
    print('{} convertido em octal é {}.'.format(n, oct(n)[2:]))
elif opcao == 3:
    print('{} convertido em hexadecimal é {}.'.format(n, hex(n)[2:]))
else:
    print('Opção inválida. Digite uma das opções válidas.')