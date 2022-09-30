Exercício 8
metro = int(input('Digite um numero: '))
decametro = metro / 10
hectometro = metro / 100
kilometro = metro / 1000
decimetro = metro * 10
centimetro = metro * 100
milimetro = metro *100
print(f'O valor em decametro é: ', decametro, 'decametros')
print(f'O valor em hectometro é: ', hectometro, 'hectometro')
print(f'O valor em kilometro é: ', kilometro, 'kilometro')
print(f'O valor em decimetro é: ', decimetro, 'decimetro')
print(f'O valor em centimetro é: ', centimetro, 'centimetro')
print(f'O valor em milimetro é: ', milimetro, 'milimetro')

Segunda forma
m = int(input('Digite um numero: '))
print('O valor em decametro é {}. O valor do hectometro é {}. O valor do quilomêtro é {}. O valor do decimetro é {}. O valor do centimetro é {}. O valor do milímetro é {}.' .format((m/10), (m/100), (m/1000), (m*10), (m*100), (m*1000)))