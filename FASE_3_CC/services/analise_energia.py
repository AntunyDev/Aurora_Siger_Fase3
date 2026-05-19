from data.dados_colonia import colonia


def calcular_gasto_energetico():
    consumo_diario = sum(colonia["consumo"].values())

    hist_e_eolica = colonia['historico']['eolica']['energia']
    hist_e_solar = colonia['historico']['solar']['energia']

    producao_total = [
        solar + eolica
        for solar, eolica in zip(hist_e_solar, hist_e_eolica)
    ]

    saldo_energetico = [
        producao - consumo_diario
        for producao in producao_total
    ]

    reserva = colonia["producao_atual"]["reserva"]
    reserva_final = reserva + sum(saldo_energetico)

    return consumo_diario, producao_total, saldo_energetico, reserva_final

def analisar_energia(geracao_total, consumo_total):
    if consumo_total > geracao_total:
        return "ALERTA: consumo maior que geração"

    elif geracao_total > consumo_total:
        return "SUGESTÃO: armazenar energia excedente"

    return "Sistema equilibrado"