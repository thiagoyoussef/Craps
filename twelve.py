def twelve(aposta,fichas,soma_dados):
    if soma_dados==12:
        fichas+=aposta*30
    else:
        fichas=fichas-aposta
    return fichas    