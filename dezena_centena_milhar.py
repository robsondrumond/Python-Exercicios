#Exercício 23 (Descobrir unidade, dezena, centena e milhar)
#Obs: Implementado loop por meio de uma função

def desmembra_numero():
    numero = int(input('Digite um número entre 0 e 9999: '))
    if numero < 9999:
        unidade = numero / 1 % 10
        dezena = numero / 10 % 10
        centena = numero / 100 % 10
        milhar = numero / 1000 % 10
        print('O numero que você digitou tem {} unidades.'.format(int(unidade)))
        print('O numero que você digitou tem {} dezenas.'.format(int(dezena)))
        print('O numero que você digitou tem {} centenas.'.format(int(centena)))
        print('O numero que você digitou tem {} milhar.'.format(int(milhar)))
    else:
        print('O numero digitado está fora do alcance')
        desmembra_numero()

desmembra_numero()
