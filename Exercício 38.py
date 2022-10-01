#Exercício 38 (Recebe 2 valores e testa qual é maior ou se ambos são iguais)
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o primeiro valor: '))

if n1 > n2:
    print('O primeiro valor é o maior')
elif n2 > n1:
    print('O segundo valor é o maior')
else:
    print('Os dois valores são iguais')