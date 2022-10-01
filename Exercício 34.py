#Exercício 34 (Recebe entrada do 'salário' e calcula o incremento)
salario = float(input('Qual o salário do colaborador? '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 110 / 100)
print('O salário do colaborador é R$ {:.2f} ' .format(novo))