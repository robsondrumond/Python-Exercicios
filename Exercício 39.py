#Exercício 39 (Recebe data de nascimento e testa se deve se alistar ou se passou do tempo ou quanto tempo falta)
from datetime import date
atual = date.today().year
nasc = int(input('Digite seu ano de nascimento: '))
alistar = atual - nasc

if alistar <= 17:
    print('Você ainda não tem idade para se alistar. Ainda faltam {} anos.' .format(atual - nasc))
elif alistar == 18:
    print('Está na hora de se alistar.')
else:
    print('Já passou da hora de se alistar.')
