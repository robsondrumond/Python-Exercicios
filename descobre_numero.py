#Exercício 30 (Descobre se o número é para ou impar)
n = int(input('Digite um número inteiro qualquer: '))
resto = n % 2
if n == 0:
    print('O número é par')
else:
    print('O número é impar')
