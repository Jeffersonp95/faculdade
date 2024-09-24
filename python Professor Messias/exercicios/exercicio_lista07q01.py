x = 0
soma_notas = 0
acumuladora = 0

while x != -1:
    x = float(input('Digite sua media ou -1 para sair do programa: '))
    
    if x != -1:
        soma_notas = soma_notas + x
        acumuladora = acumuladora + 1
        
        
media = soma_notas / acumuladora

print(media)