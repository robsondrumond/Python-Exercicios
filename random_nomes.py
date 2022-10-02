#Exercício 19 (Escolha aleatoria de nome)
import random
sorteio = []
primeiro = str(input('Digite o primeiro nome: '))
sorteio.append(primeiro)
segundo = str(input('Digite o segundo nome: '))
sorteio.append(segundo)
terceiro = str(input('Digite o terceiro nome: '))
sorteio.append(terceiro)
quarto = str(input('Digite o quarto nome: '))
sorteio.append(quarto)
escolhido = random.choice(sorteio)
print(f'O nome escolhido foi: {escolhido}')

2.ª forma
import random
n1 = str(input('Digite o primeiro nome:'))
n2 = str(input('Digite o segundo nome:'))
n3 = str(input('Digite o terceiro nome:'))
n4 = str(input('Digite o quarto nome:'))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O nome escolhido foi: {}' .format(escolhido))
