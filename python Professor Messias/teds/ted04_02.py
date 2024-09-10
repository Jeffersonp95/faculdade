fruta_proibida = int(input('Quantos frutos proibidos você quer?  : '))

if fruta_proibida >= 12:
    valor = 1.00
else:
    valor = 1.30

valor_fruto_proibido = fruta_proibida * valor

print(f'O valor da compra é de: R$ {valor_fruto_proibido:.2f}')