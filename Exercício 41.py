#Exercício 41 (Recebe ano do nascimento e verifica em qual categoria se enquadra)
from datetime import date
ano = date.today().year
nasc = int(input('Digite o ano do seu nascimento: '))
categoria = ano - nasc
if categoria < 9:
    print('O aluno tem {} anos e sua categoria é mirim.' .format(categoria))
elif categoria < 14:
    print('O aluno tem {} anos e sua categoria é infantil.'.format(categoria))
elif categoria < 19:
    print('O aluno tem {} anos e sua categoria é junior.'.format(categoria))
else:
    print('O aluno tem {} anos e sua categoria é senior.'.format(categoria))