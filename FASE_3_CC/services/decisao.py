def tomar_decisao(energia_total, consumo_total):
    if energia_total < 30:
        return "MODO CRÍTICO: desligar sistemas não essenciais"

    if energia_total < 50 and consumo_total > 60:
        return "Ativar modo economia"

    if energia_total < 50:
        return "Reduzir consumo"

    return "Sistema estável"