Exercício 6 (Mostrar dobro, triplo e raiz quadrada)
numero = int(input('Digite um numero: '))
dobro = numero * 2
triplo = pow(numero, (1/2))
raiz_quadrada = numero ** (1/2)
print('O dobro é {}. O triplo é {}. A raiz quadrada é {}.' .format(numero, dobro, triplo, raiz_quadrada))

Segunda forma
n = int(input('Digite um numero: '))
print('O dobro é {}. O triplo é {}.A raiz quadrada é {}' .format((n * 2), (n * 3), (n ** (1/2))))
