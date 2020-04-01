def field(aposta,fichas):
    soma_dados=random.randint(1,6)+random.randint(1,6)
    if soma_dados==5 or soma_dados==6 or soma_dados==7 or soma_dados==8:
        fichas=fichas-aposta
    elif soma_dados==3 or soma_dados==4 or soma_dados==9 or soma_dados==10 or soma_dados==11:
        fichas+=aposta
    elif soma_dados==2:
        fichas+=aposta*2
    elif soma_dados==12:
        fichas+=aposta*3
    return fichas
    