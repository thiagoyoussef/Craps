import random 
fichas=500
tipo_aposta = input("Você irá fazer uma aposta(retorne com o número correspondente): \nPass Line Bet(1)\nField(2)\nAny Craps(3)\nTwelve(4)\n")
aposta = int(input("Quantas fichas você deseja apostar? "))
soma_dados=random.randint(1,6)+random.randint(1,6)     