Exercício 13 (Aumento com porcentagem)
salario = float(input('Qual é o salário do funcionário? R$ '))
aumento = salario + (salario * 15 / 100)
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, vai ganhar R${:.2f}' .format(salario, aumento))