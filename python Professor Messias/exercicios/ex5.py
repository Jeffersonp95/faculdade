agua = int(input('Quantidade de água disponível: '))
distancia = int(input('Distância até o oásis: '))

quantidade_agua = distancia * 2

if agua >= quantidade_agua:
    print('A água é suficiente.')
else:
    print('A água não é suficiente.')