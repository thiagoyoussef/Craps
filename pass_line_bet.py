def pass_line_bet(aposta,fichas,soma_dados):
    if soma_dados==7 or soma_dados==11:
        fichas+=aposta
    elif soma_dados==2 or soma_dados==3 or soma_dados==12:
        fichas=fichas-aposta
    elif soma_dados==4 or soma_dados==5 or soma_dados==6 or soma_dados==8 or soma_dados==9 or soma_dados==10:
        return("Ainda não sei")