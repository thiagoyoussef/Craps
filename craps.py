import random 
fichas=500
tipo_aposta = input("Você irá fazer uma aposta: \nPass Line Bet\nField\nAny Craps\nTwelve\n")
aposta = int(input("Quantas fichas você deseja apostar? "))
soma_dados=random.randint(1,6)+random.randint(1,6)
    if soma_dados==12:
        fichas+=aposta*30
    else:
