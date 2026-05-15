# modelo_previsao.py

from dados_colonia import historico_clima

def treinar_modelo():
    """
    Calcula a Regressão Linear (y = mx + b) usando o método dos Mínimos Quadrados.
    Demonstra entendimento matemático sem bibliotecas externas.
    """
    x = historico_clima["vento"]
    y = historico_clima["energia"]
    n = len(x)

    # Cálculos necessários para a fórmula
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum(val_x * val_y for val_x, val_y in zip(x, y))
    sum_x_quad = sum(val_x**2 for val_x in x)

    # Cálculo da Inclinação (m)
    # m = (n*sum(xy) - sum(x)*sum(y)) / (n*sum(x^2) - (sum(x))^2)
    m = (n * sum_xy - sum_x * sum_y) / (n * sum_x_quad - sum_x**2)

    # Cálculo do Intercepto (b)
    # b = (sum(y) - m*sum(x)) / n
    b = (sum_y - m * sum_x) / n

    return m, b

def prever_energia(vento_futuro):
    """Realiza a estimativa baseada na reta ajustada."""
    m, b = treinar_modelo()
    previsao = (m * vento_futuro) + b
    previsao = max(0, previsao)

    print(f"\n--- MODELO DE PREVISÃO ENERGÉTICA ---")
    print(f"Equação da Reta Ajustada: y = {m:.2f}x + {b:.2f}")
    print(f"Entrada (Vento): {vento_futuro} m/s")
    print(f"Saída (Energia Estimada): {previsao:.2f} unidades")
    
    return previsao
