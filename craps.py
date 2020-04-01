
#funcao pass line bet come out
def pass_line_bet_come_out(aposta,fichas):
    soma_dados=random.randint(1,6)+random.randint(1,6)
    if soma_dados==7 or soma_dados==11:
        fichas+=aposta*2
        return fichas
    elif soma_dados==2 or soma_dados==3 or soma_dados==12:
        fichas=fichas
        return fichas
    elif soma_dados==4 or soma_dados==5 or soma_dados==6 or soma_dados==8 or soma_dados==9 or soma_dados==10:
        return True

#funcao pass line bet point

#funcao anycraps
def any_craps(aposta,fichas):
    soma_dados=random.randint(1,6)+random.randint(1,6)
    if soma_dados == 2 or soma_dados == 3 or soma_dados == 12:
        fichas += (7*aposta)+aposta
    else:
        fichas=fichas
    return fichas

#função field
def field(aposta,fichas):
    soma_dados=random.randint(1,6)+random.randint(1,6)
    if soma_dados==5 or soma_dados==6 or soma_dados==7 or soma_dados==8:
        fichas=fichas
    elif soma_dados==3 or soma_dados==4 or soma_dados==9 or soma_dados==10 or soma_dados==11:
        fichas+=aposta*2
    elif soma_dados==2:
        fichas+=aposta*2+aposta
    elif soma_dados==12:
        fichas+=aposta*3+aposta
    return fichas

#função twelve
def twelve(aposta,fichas):
    soma_dados=random.randint(1,6)+random.randint(1,6)
    if soma_dados==12:
        fichas+=aposta*30+aposta
    else:
        fichas=fichas
    return fichas

import random 
fichas=500
quer_sair = False
estaPoint = False
estaComeout = True
while quer_sair == False and fichas > 0:
    sair = input('Gostaria de sair do jogo? ')
    
    if sair == 'sim' or sair == 'Sim':
        quer_sair = True
    else: #A partir desse else temos a fase comeout
        print('Voce esta na fase Come out')
        print(fichas)
        aposta = [0]*4
        aposta_adc = 's'
        while aposta_adc=="s":
            tipo_aposta = (int(input("Qual aposta desejas fazer? (retorne com o número correspondente): \nPass Line Bet(0)\nField(1)\nAny Craps(2)\nTwelve(3)\n")))
            aposta[tipo_aposta] = int(input("Quantas fichas você deseja apostar? "))
            fichas-=aposta[tipo_aposta]
            aposta_adc=input("Você deseja realizar outro tipo de aposta? (s/n) ")
        if aposta[0] != 0: #se vai rodar o pass_line_bet_come_out
            print(pass_line_bet_come_out(aposta[0],fichas))

        if aposta[1] != 0: #se vai rodar o field
            print(field(aposta[1],fichas))
        if aposta[2] != 0: #se vai rodar o any craps
            print(any_craps(aposta[2],fichas))

        if aposta[3] != 0: #se vai rodar o twelve
            print(twelve(aposta[3],fichas))
        aposta.clear()
        