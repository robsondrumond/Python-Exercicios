#Exercício 43 (Cáluco do IMC com informação do peso)
peso = int(input('Digite seu peso: '))
altura = float(input('Digite seu altura: '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Seu imc é de {:.2f}. Você está abaixo do peso.' .format(imc))
elif imc <= 18.5 and imc < 25:
    print('Seu imc é de {:.2f}. Você está no peso ideal.' .format(imc))
elif imc <= 25 and imc < 40:
    print('Seu imc é de {:.2f}. Você está em sobrepeso.' .format(imc))
elif imc >= 40:
    print('Seu imc é de {:.2f}. Você está obeso.' .format(imc))
else:
    print('Seu imc é de {:.2f}. Você está em obesidade mórbida.' .format(imc))