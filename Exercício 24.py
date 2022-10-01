#Exercício 24 (Acertar o nome da cidade)

def descobre_cidade():

    cidade = str(input('Qual cidade você nasceu? '))
    if cidade == 'Nova Iguaçu':
        print('Você nasceu em {}' .format(cidade))
    else:
        print('Você não nasceu nessa cidade. Tente novamente.')
        descobre_cidade()

descobre_cidade()

nome = str(input('Digite o nome da sua cidade:')).strip()
divisao = nome.upper().split()
print('NOVA IGUAÇU' in divisao)