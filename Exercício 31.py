#Exercício 31 (Testar condição e calcular distância)
distancia = int(input('Qual a distância da viagem em KM?  '))
if distancia <= 200:
    print(f'O valor da viagem é de {distancia * 0.50}')
else:
    print(f'O valor da viagem é de {distancia * 0.45}')
