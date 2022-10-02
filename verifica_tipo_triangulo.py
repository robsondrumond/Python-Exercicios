#Exercício 42 (Recebe 3 medidas, verifica se formam um triângulo e qual ele é)
print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)
m1 = float(input('Primeiro segmento: '))
m2 = float(input('Segundo segmento: '))
m3 = float(input('Terceiro segmento: '))
if m1 < m2 + m3 and m2 < m1 + m3 and m3 < m2 + m1:
    print('Os segmentos acima PODEM FORMAR UM TRIANGULO')
    if m1 == m2 == m3:
        print('O triângulo formado é Equilátero')
    elif m1 != m2 != m3 != m1:
        print('O triângulo formado é Isósceles')
    else:
        print('O triângulo formado é Escaleno')
else:
    print('Os segmentos acima NÃO PODEM FORMAR UM TRIANGULO')
