from random import randint

espada_ataque = randint(50, 200)
espada_durabilidade = randint(51, 120)

arco_ataque = randint(42, 100)
arco_durabilidade = randint(30, 120)

lanca_ataque = randint(44, 166)
lanca_durabilidade = randint(51, 156)

if espada_ataque > 50 and espada_durabilidade > 70:
    print('Espada')
elif arco_ataque > 50 and arco_durabilidade > 70:
    print('Arco')
elif lanca_ataque > 50 and lanca_durabilidade >70:
    print('Lança')
else:
    print('Escolha outra arma')