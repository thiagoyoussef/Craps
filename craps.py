import random 
fichas=500
tipo_aposta = int(input("Você irá fazer uma aposta(retorne com o número correspondente): \nPass Line Bet(1)\nField(2)\nAny Craps(3)\nTwelve(4)\n"))
aposta = int(input("Quantas fichas você deseja apostar? "))
soma_dados=random.randint(1,6)+random.randint(1,6)
quer_sair = False
while quer_sair == False or fichas != 0:
    sair = input('Gostaria de sair do jogo? ')
    if sair == 'sim' or sair == 'Sim':
        quer_sair = True
    else:
        if tipo_aposta==1