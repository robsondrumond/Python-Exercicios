#Exercício 15 (Calculo de km/dia rodado)
km = float(input('Informe a quantidade de quilometros rodados: '))
dias = int(input('Informe quantos dias o carro foi usado: '))
total = (dias * 60) + (km * 0.15)
print('O total a pagar é R${:.2f}' .format(total))