from utils.helpers import mostrar_titulo
from services.previsao import calcular_producao
from services.analise_energia import calcular_gasto_energetico, analisar_energia
from services.decisao import tomar_decisao


def main():
    mostrar_titulo()

    exposicao = int(input("Exposição solar (horas): "))
    vento = int(input("Velocidade do vento: "))

    # Previsão de produção do dia
    solar, eolica = calcular_producao(vento, exposicao)

    # Dados históricos e consumo
    consumo_total, producao_total, saldo_energetico, reserva = calcular_gasto_energetico()

    # Produção do dia (sem reserva)
    geracao_hoje = solar + eolica

    # Energia disponível total = produção atual + reserva acumulada
    energia_disponivel = geracao_hoje + reserva

    # Resultado final após consumo
    saldo_final = energia_disponivel - consumo_total

    print(f"Produção solar prevista: {solar:.2f}")
    print(f"Produção eólica prevista: {eolica:.2f}")
    print(f"Geração total de hoje: {geracao_hoje:.2f}")
    print(f"Reserva acumulada: {reserva:.2f}")
    print(f"Energia disponível total: {energia_disponivel:.2f}")
    print(f"Consumo total: {consumo_total}")
    print(f"Produção histórica: {producao_total}")
    print(f"Saldo histórico: {saldo_energetico}")
    print(f"Saldo final do dia: {saldo_final:.2f}")

    print(analisar_energia(energia_disponivel, consumo_total))
    print(tomar_decisao(energia_disponivel, consumo_total))


if __name__ == "__main__":
    main()