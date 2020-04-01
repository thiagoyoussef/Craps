
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
        tipo_aposta=[]
        tipo_aposta.append(int(input("Qual aposta desejas fazer? (retorne com o número correspondente): \nPass Line Bet(1)\nField(2)\nAny Craps(3)\nTwelve(4)\n")))
        aposta = int(input("Quantas fichas você deseja apostar? "))
        aposta_adc=input("Você deseja realizar outro tipo de aposta? (s/n) ")
        fichas-=aposta
        if aposta_adc=="s":
            tipo_aposta.append(int(input("Qual aposta desejas fazer? (retorne com o número correspondente): \nPass Line Bet(1)\nField(2)\nAny Craps(3)\nTwelve(4)\n")))
        else:
            if tipo_aposta[0]==1 or tipo_aposta[1]==1 or tipo_aposta[2]==1 or tipo_aposta[3]==1:
                print(pass_line_bet_come_out(aposta,fichas))
                if pass_line_bet_come_out==True:
                    aposta_adc=input("Você deseja realizar outro tipo de aposta? (s/n) ")
                    
            elif tipo_aposta[0]==2 or tipo_aposta[1]==2 or tipo_aposta[2]==2 or tipo_aposta[3]==2:
                field(aposta,fichas)
            elif tipo_aposta[0]==3 or tipo_aposta[1]==3 or tipo_aposta[2]==3 or tipo_aposta[3]==3:
                any_craps(aposta,fichas)
            elif tipo_aposta[0]==4 or tipo_aposta[1]==4 or tipo_aposta[2]==4 or tipo_aposta[3]==4:
                twelve(aposta,fichas)