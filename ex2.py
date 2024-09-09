ferro = float(input('ferro: '))
ouro = float(input('ouro: '))

peso_total = ferro + ouro

if peso_total > 0:
    porcentagem_ferro = (ferro / peso_total) * 100

    if porcentagem_ferro >= 70:
        print('A liga tem pelo menos 70% de ferro. É suficiente.')

    else:
        print(' a liga tem menos de 70% de ferro. É insificiente.')
else:
    print("As quantidades de ferro e ouro devem ser maiores que zero.")
