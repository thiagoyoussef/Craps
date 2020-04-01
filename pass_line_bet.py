def pass_line_bet(aposta,fichas,soma_dados):
    estaComeout = True
    if soma_dados==7 or soma_dados==11:
        fichas+=aposta
    elif soma_dados==2 or soma_dados==3 or soma_dados==12:
        fichas=fichas-aposta
    elif soma_dados==4 or soma_dados==5 or soma_dados==6 or soma_dados==8 or soma_dados==9 or soma_dados==10:
        estaComeout=False
        estaPoint=True
        tipo_aposta = int(input("Você irá fazer uma aposta(retorne com o número correspondente): \nPass Line Bet(1)\nField(2)\nAny Craps(3)\nTwelve(4)\n"))
        aposta = int(input("Quantas fichas você deseja apostar? "))
