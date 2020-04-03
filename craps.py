#Dupla:
#Arthur Chieppe
#Thiago Youssef

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

#variaveis globais
import random 
fichas=500
quer_sair = False
estaPoint = False
estaComeout = True
aposta=[]
boole = False
#Início do jogo
print('Bem-vindo ao Craps!')
while quer_sair == False and fichas > 0:
    print('Você tem {} fichas' .format(fichas))
    sair = input('Gostaria de sair do jogo? (s/n) ')
    if sair =='s':
        quer_sair = True
        break
    print('Voce esta na fase Come out')
    print('Você tem {} fichas' .format(fichas))
    aposta = [0]*4
    aposta_adc = 's'
    while aposta_adc=="s":
        tipo_aposta = (int(input("Qual aposta desejas fazer? (digite o número correspondente): \nPass Line Bet(0)\nField(1)\nAny Craps(2)\nTwelve(3)\n")))
        aposta[tipo_aposta] = int(input("Quantas fichas você deseja apostar? "))
        if sum(aposta) > fichas: #valida apostas
            print('Você apostou mais fichas do que possui! \nRealize todas as apostas novamente:')
            aposta[0] = 0
            aposta[1] = 0
            aposta[2] = 0
            aposta[3] = 0
            continue
        aposta_adc=input("Você deseja realizar outro tipo de aposta? (s/n) ")
    fichas-=aposta[0] #após a soma das apostas serem validadas, o valor de cada aposta é subtraído das ficas
    fichas-=aposta[1]
    fichas-=aposta[2]
    fichas-=aposta[3]
    if aposta[1] != 0: #se vai rodar o field
        fichas = field(aposta[1],fichas)
        print("Na aposta Field você terminou com {} fichas".format(fichas))
    if aposta[2] != 0: #se vai rodar o any craps
        fichas = field(aposta[2],fichas)
        print("Na aposta Any Craps você terminou com {} fichas".format(fichas))
    if aposta[3] != 0: #se vai rodar o twelve
        fichas = field(aposta[3],fichas)
        print("Na aposta Twelve você terminou com {} fichas".format(fichas))
    if fichas <= 0:
        quer_sair = True
        break
    if aposta[0] != 0: #se vai rodar o pass_line_bet_come_out
        boole = False
        retorno=(pass_line_bet_come_out(aposta[0],fichas))
        boole = retorno[0] #boolean se entrou na fase point
        fichas = retorno[1] #fichas que sairam da funcao
        point = retorno[2] #valor da point obtido no come out
        x=0
        while boole==True and x==0: #Entrando na fase point
            print('Voce esta na fase Point')
            print("O valor do Point é {0}".format(point))
            soma_dados=random.randint(1,6)+random.randint(1,6)
            if point==soma_dados:
                fichas+=aposta[0]*2
                x=1
                print("Os dados foram jogados automaticamente e você ganhou o Point e saiu com {} fichas!".format(fichas))
                continue
            elif soma_dados==7:
                fichas=fichas
                x=1
                print("Os dados foram jogados automaticamente e você perdeu o Point e saiu com {} fichas!".format(fichas))
                continue
            else:
                x=0
                print("Os dados foram jogados automaticamente e o resultado foi diferente de {} e 7!".format(point))
            
            aposta[1]=0 #limpando apostas feitas anteriormente
            aposta[2]=0
            aposta[3]=0
            print('Você tem {} fichas' .format(fichas))
            aposta_adc=input("Você deseja realizar outro tipo de aposta antes de jogar os dados novamente? (s/n) ")
            while aposta_adc=="s":
                tipo_aposta = (int(input("Qual aposta desejas fazer? (digite o número correspondente): \nField(1)\nAny Craps(2)\nTwelve(3)\n")))
                aposta[tipo_aposta] = int(input("Quantas fichas você deseja apostar? "))
                if (aposta[1] + aposta[2] + aposta[3]) > fichas: #valida apostas
                    print('Você apostou mais fichas do que possui! \nRealize todas as apostas novamente:')
                    aposta[1] = 0
                    aposta[2] = 0
                    aposta[3] = 0
                    continue
                aposta_adc=input("Você deseja realizar outro tipo de aposta? (s/n) ")
            fichas-=aposta[1] #após a soma das apostas serem validadas, o valor de cada aposta é subtraído das fichas
            fichas-=aposta[2]
            fichas-=aposta[3]
            if aposta[1] != 0: #se vai rodar o field
                fichas = field(aposta[1],fichas)
                print("Na aposta Field você terminou com {} fichas".format(fichas))
            if aposta[2] != 0: #se vai rodar o any craps
                fichas = any_craps(aposta[2],fichas)
                print("Na aposta Any Craps você terminou com {} fichas".format(fichas))
            if aposta[3] != 0: #se vai rodar o twelve
                fichas = twelve(aposta[3],fichas)
                print("Na aposta Twelve você terminou com {} fichas".format(fichas))
            if fichas <= 0: #checar se ainda tem fichas dentro do while do point
                quer_sair = True
                break
    if fichas <= 0: #checar se ainda tem fichas fora do while do point
        quer_sair = True
        break
    aposta.clear()
if fichas > 0: #determina a frase de encerramento adequada
    print('Você terminou o jogo com {} fichas' .format(fichas))
else:
    print('Que pena, suas fichas acabaram!')