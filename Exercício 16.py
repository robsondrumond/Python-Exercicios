#Exercício 16 (Obter porção inteira de um número)
n = float(input('Digite um número: '))
print('O valor digitado foi de {}. A sua porção inteira é {}' .format(n, int(n)))

from math import trunc
n = float(input('Digite um número: '))
print('O valor digitado foi de {}. A sua porção inteira é {}' .format(n, trunc(n)))