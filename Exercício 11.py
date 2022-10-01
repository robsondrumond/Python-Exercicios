Exercício 11 (Calculo de dimensões)
l = float(input('Digite a largura da parede: '))
a = float(input('Digite a altura da parede: '))
d = l*a
t = d / 2
print('Sua parede tem a dimensão de {}x{} e sua área é de {:.3f}m².' .format(l, a, d))
print('Para pintar essa parede, você precisará de {:.2f}m².' .format(t))