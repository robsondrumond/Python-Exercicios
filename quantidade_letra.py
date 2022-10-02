#Exercício 26 (Mostre quantas vezes aparece a letra A, qual a primeira posição e a última)

nome = str(input('Digite uma frase: ')) .upper()
print('A letra A apareceu {} vezes' .format(nome.count('A')))
print('A letra A apareceu primeiro na posição {}' .format(nome.find('A')+1))
print('A letra A apareceu primeiro na posição {}' .format(nome.rfind('A')+1))
