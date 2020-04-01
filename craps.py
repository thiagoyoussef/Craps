import random 
fichas=500
quer_sair = False
estaPoint = False
estaComeout = True

#funcao pass line bet come out
def pass_line_bet_come_out(aposta,fichas):
    soma_dados=random.randint(1,6)+random.randint(1,6)
    if soma_dados==7 or soma_dados==11:
        fichas+=aposta
        return fichas
    elif soma_dados==2 or soma_dados==3 or soma_dados==12:
        fichas=fichas-aposta
        return fichas
    elif soma_dados==4 or soma_dados==5 or soma_dados==6 or soma_dados==8 or soma_dados==9 or soma_dados==10:
        return True

#funcao anycraps
def any_craps(aposta, soma_dados, fichas):
    if soma_dados == 2 or soma_dados == 3 or soma_dados == 12:
        fichas += (7*aposta)
    else:
        fichas -= aposta
    return fichas



while quer_sair == False or fichas > 0:
    sair = input('Gostaria de sair do jogo? ')
    if sair == 'sim' or sair == 'Sim':
        quer_sair = True
    else: #A partir desse else temos a fase comeout
        print('Voce esta na fase Come out')
        tipo_aposta=[]
        append.tipo_aposta(int(input("Qual aposta desejas fazer? (retorne com o número correspondente): \nPass Line Bet(1)\nField(2)\nAny Craps(3)\nTwelve(4)\n")))
        aposta = int(input("Quantas fichas você deseja apostar? "))
        aposta_adc=input("Você deseja realizar outro tipo de aposta? (s/n) ")
        fichas-=aposta
        if aposta_adc=="s":
            append.tipo_aposta(int(input("Qual aposta desejas fazer? (retorne com o número correspondente): \nPass Line Bet(1)\nField(2)\nAny Craps(3)\nTwelve(4)\n")))
        else:
            if tipo_aposta[0]==1 or tipo_aposta[1]==1 or tipo_aposta[2]==1 or tipo_aposta[3]==1:
                pass_line_bet_come_out(aposta,fichas)
            elif tipo_aposta[0]==2 or tipo_aposta[1]==2 or tipo_aposta[2]==2 or tipo_aposta[3]==2:
                field(aposta,fichas)