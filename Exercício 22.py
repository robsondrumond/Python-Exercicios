#Exercício 22 (Peça um nome e converta para letras maiúsculas e minusculas. Conte quantas letras tem o nome todo e o primeiro nome)
nome = str(input('Digite seu nome completo:'))
print('Analisando seu nome...')
print('Seu nome em letras maiusculas fica:{}' .format(nome.upper()))
print('Seu nome em letras minuscula fica:{}' .format(nome.lower()))
print('Seu nome tem ao todo {} letras.' .format(len(nome) - nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e tem {} letras.' .format(separa[0], len(separa[0])))
