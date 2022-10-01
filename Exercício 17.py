#Exercício 17 (Calculo da hipotenusa)
from math import hypot
c1 = float(input('Informe o valor do cateto oposto:'))
c2 = float(input('Informe o valor do cateto adjacente:'))
print('A hipotenusa vai medir: {:.2f}' .format(hypot(c1, c2)))