
#funcao pass line bet come out
def pass_line_bet_come_out(aposta,fichas):
    soma_dados=random.randint(1,6)+random.randint(1,6)
    point=soma_dados
    if soma_dados==7 or soma_dados==11:
        fichas+=aposta*2
        return False, fichas, 0
    elif soma_dados==2 or soma_dados==3 or soma_dados==12:
        fichas=fichas
        return False, fichas, 0
    elif soma_dados==4 or soma_dados==5 or soma_dados==6 or soma_dados==8 or soma_dados==9 or soma_dados==10:
        return bool(True),fichas , int(point)


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
aposta=[]
while quer_sair == False and fichas > 0:
    sair = input('Gostaria de sair do jogo? ')
    
    if sair == 'sim' or sair == 'Sim' or sair =='s':
        quer_sair = True
    else: #A partir desse else temos a fase comeout
        print('Voce esta na fase Come out')
        print('Você tem {} fichas' .format(fichas))
        aposta = [0]*4
        aposta_adc = 's'
        while aposta_adc=="s":
            tipo_aposta = (int(input("Qual aposta desejas fazer? (retorne com o número correspondente): \nPass Line Bet(0)\nField(1)\nAny Craps(2)\nTwelve(3)\n")))
            aposta[tipo_aposta] = int(input("Quantas fichas você deseja apostar? "))
            if sum(aposta) > fichas:
                print('Você apostou mais ficahs do que possui! \nRealize todas as apostas novamente:')
                aposta[0] = 0
                aposta[1] = 0
                aposta[2] = 0
                aposta[3] = 0
                continue
            aposta_adc=input("Você deseja realizar outro tipo de aposta? (s/n) ")
        fichas-=aposta[0]
        fichas-=aposta[1]
        fichas-=aposta[2]
        fichas-=aposta[3]
        if aposta[1] != 0: #se vai rodar o field
            print(field(aposta[1],fichas))
        if aposta[2] != 0: #se vai rodar o any craps
            print(any_craps(aposta[2],fichas))
        if aposta[3] != 0: #se vai rodar o twelve
            print(twelve(aposta[3],fichas))
        if aposta[0] != 0: #se vai rodar o pass_line_bet_come_out
            boole = False
            retorno=(pass_line_bet_come_out(aposta[0],fichas))
            boole = retorno[0] #boolean se entrou na fase point
            fichas = retorno[1]
            point = retorno[2] #valor da point obtido no come out
            x=0
            while boole==True and x==0:
                print('Voce esta na fase Point')
                print("O valor do Point é {0}".format(point))
                aposta_adc=input("Você deseja realizar outro tipo de aposta? (s/n) ")
                if aposta_adc=="n":
                    soma_dados=random.randint(1,6)+random.randint(1,6)
                    if point==soma_dados:
                        fichas+=aposta[0]*2
                        x=1
                    elif soma_dados==7:
                        fichas=fichas
                        x=1
                    else:
                        x=0
                else:
                    aposta[1]=0
                    aposta[2]=0
                    aposta[3]=0
                    tipo_aposta = (int(input("Qual aposta desejas fazer? (retorne com o número correspondente): \nField(1)\nAny Craps(2)\nTwelve(3)\n")))
                    aposta[tipo_aposta] = int(input("Quantas fichas você deseja apostar? "))
                    fichas-=aposta[tipo_aposta]
                    if aposta[1] != 0: #se vai rodar o field   
                            print(field(aposta[1],fichas))
                    if aposta[2] != 0: #se vai rodar o any craps
                            print(any_craps(aposta[2],fichas))
                    if aposta[3] != 0: #se vai rodar o twelve
                            print(twelve(aposta[3],fichas))
    aposta.clear()