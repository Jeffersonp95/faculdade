altura = float(input('Altura da planta: '))

altura_planta = altura

if altura_planta < 1:
    print('A planta é pequena.')
elif altura_planta > 1 or altura_planta <= 3:
    print('A planta é média.')
else:
    print('A planta é grande') 