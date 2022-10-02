Exercício 12 (Desconto com porcentagem)
preco = float(input('Qual é o preço do produto? R$ '))
desconto = preco - (preco * 5 / 100)
print('O produto que custava R${:.2f}, na promoção, com o desconto de 5%, vai custar R${:.2f}' .format(preco, desconto))
