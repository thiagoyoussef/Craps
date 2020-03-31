def any_craps(aposta, soma_dados, fichas):
    if soma_dados == 2 or soma_dados == 3 or soma_dados == 12:
        fichas += (7*aposta)
    else:
        fichas -= aposta
    return fichas