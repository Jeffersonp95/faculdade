dragao_um_distancia = float(input('Distância do primeiro dragão: '))
dragao_um_tempo = float(input('Tempo do primeiro drgão: '))

dragao_dois_distancia = float(input('Distância do segundo dragão: '))
dragao_dois_tempo = float(input('Tempo do segundo drgão: '))

velocidade_dragao_um = dragao_um_distancia / dragao_um_tempo
velocidade_dragao_dois = dragao_dois_distancia / dragao_dois_tempo

if velocidade_dragao_um > velocidade_dragao_dois:
    print('O Primeiro dragão é mais rápido.')
elif velocidade_dragao_dois > velocidade_dragao_um:
    print('O segundo dragão é mais rápido.')
else:
    print('Os dragões tem a mesma velocidade')