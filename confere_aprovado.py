#Exercício 40 (Recebe 2 notas e testa se foi aprovado ou não)
nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
media = (nota1 + nota2) / 2
if media < 5.0:
    print('Sua média foi {} e você está REPROVADO!' .format(media))
elif media > 5.0 and media < 6.9:
    print('Sua média foi {} e você está RECUPERAÇÃO!' .format(media))
else:
    print('Sua média foi {} e você está APROVADO!' .format(media))
