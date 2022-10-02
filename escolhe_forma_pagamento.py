#Exercício 44 (Recebe preço e escolha de opção e informa descontos com base na forma de pagamento)
preco = float(input('Digite o preço do produto: R$ '))
escolha = int(input(
'''Escolha a forma de pagamento:
[ 1 ] á vista dinheiro/cheque: 10% de desconto
[ 2 ] à vista no cartão: 5% de desconto
[ 3 ] em até 2x no cartão
[ 4 ] 3x ou mais no cartão: 20% de juros: '''))

if escolha == 1:
    avista = (preco * 10 / 100) - preco
    print('O produto que custava R${:.2f}, com desconto do preço a vista, fica R${:.2f}.' .format(preco, avista))
elif escolha == 2:
    cartao = avista = (preco * 5 / 100) - preco
    print('O produto que custava R${:.2f}, com desconto do cartão, fica R${:.2f}.'.format(preco, cartao))
elif escolha == 3:
    print('Nesta forma de pagamento não há desconto. O preço é de R$ {:.2f}.' .format(preco))
elif escolha == 4:
    juros = (preco * 20 / 100) + preco
    print('O produto que custava R${:.2f}, com juros do cartão, fica R${:.2f}.'.format(preco, juros))
else:
    print('Opção inválida. Escolha novamente.')
