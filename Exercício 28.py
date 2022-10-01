#Exercício 29 (Jogo de advinha qual o número de 0 a 5)

from random import randint
computador = randint(0, 5)
print('-=-' * 10)
print('Vou pensar em um número de 0 a 5. Tende advinhar qual é!')
print('-=-' * 10)
jogador = int(input('Em que número eu pensei... '))

if jogador == computador:
    print('Parabéns! Você ganhou o jogo!')
else:
    print('Ganhei! Mais sorte na próxima vez')