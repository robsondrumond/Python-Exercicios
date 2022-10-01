#Exercício 35 (Recebe a entrada de 3 medidas e verifica se forma um triângulo ou não)
print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)
m1 = float(input('Primeiro segmento: '))
m2 = float(input('Segundo segmento: '))
m3 = float(input('Terceiro segmento: '))
if m1 < m2 + m3 and m2 < m1 + m3 and m3 < m2 + m1:
    print('Os segmentos acima PODEM FORMAR UM TRIÂNGULO')
else:
    print('Os segmentos acima NÃO PODEM FORMAR UM TRIÂNGULO')