import random 
fichas=500

soma_dados=random.randint(1,6)+random.randint(1,6)
quer_sair = False
estaPoint = False
estaComeout = True

while quer_sair == False or fichas != 0:
    sair = input('Gostaria de sair do jogo? ')
    if sair == 'sim' or sair == 'Sim':
        quer_sair = True
    else: #A partir desse else temos a fase comeout
        print('Voce esta na fase Come out')
        tipo_aposta = int(input("Você irá fazer uma aposta(retorne com o número correspondente): \nPass Line Bet(1)\nField(2)\nAny Craps(3)\nTwelve(4)\n"))
        aposta = int(input("Quantas fichas você deseja apostar? "))
        if soma_dados==7 or soma_dados==11:
            fichas+=aposta
        elif soma_dados==2 or soma_dados==3 or soma_dados==12:
            fichas=fichas-aposta
        elif soma_dados==4 or soma_dados==5 or soma_dados==6 or soma_dados==8 or soma_dados==9 or soma_dados==10:
            estaComeout=False
            estaPoint=True
            tipo_aposta = int(input("Você irá fazer uma aposta(retorne com o número correspondente): \nPass Line Bet(1)\nField(2)\nAny Craps(3)\nTwelve(4)\n"))
            aposta = int(input("Quantas fichas você deseja apostar? "))