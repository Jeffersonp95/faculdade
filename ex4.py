
quantidade_reais = int(input("Quantidade de moedas de 1 real: "))
quantidade_cinquenta_centavos = int(input("Quantidade de moedas de 50 centavos: "))
quantidade_vinte_e_cinco_centavos = int(input("Quantidade de moedas de 25 centavos: "))


valor_reais = 1.00
valor_cinquenta_centavos = 0.50
valor_vinte_e_cinco_centavos = 0.25


valor_total = (quantidade_reais * valor_reais +
               quantidade_cinquenta_centavos * valor_cinquenta_centavos +
               quantidade_vinte_e_cinco_centavos * valor_vinte_e_cinco_centavos)


print(f"Valor total das moedas: R$ {valor_total:.2f}")
