tipo_animal = input("Seu animal favorito é um mamífero ou réptil? (Digite 'mamífero' ou 'réptil'): ").strip().lower()


if tipo_animal == 'mamífero':
    print("Seu animal favorito deve ser um cachorro!")
elif tipo_animal == 'réptil':
    print("Seu animal favorito deve ser uma tartaruga!")
else:
    print("Resposta inválida. Por favor, responda com 'mamífero' ou 'réptil'.")