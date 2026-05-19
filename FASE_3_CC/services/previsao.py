from sklearn.linear_model import LinearRegression
from data.dados_colonia import colonia


def calcular_producao(vento, exposicao_solar):
    # Solar
    hist_exp = colonia["historico"]["solar"]["exposicao_horas"]
    hist_e_solar = colonia["historico"]["solar"]["energia"]

    X = [[valor] for valor in hist_exp]
    y = hist_e_solar

    modelo = LinearRegression()
    modelo.fit(X, y)

    previsao_solar = modelo.predict([[exposicao_solar]])[0]

    # Eólica
    hist_vento = colonia["historico"]["eolica"]["vento"]
    hist_e_eolica = colonia["historico"]["eolica"]["energia"]

    X1 = [[valor] for valor in hist_vento]
    y1 = hist_e_eolica

    modelo1 = LinearRegression()
    modelo1.fit(X1, y1)

    previsao_eolica = modelo1.predict([[vento]])[0]

    ##Adicionando nas listas
    #Solar
    hist_exp.append(exposicao_solar)
    hist_e_solar.append(round(previsao_solar))
    #Eolica
    hist_vento.append(vento)
    hist_e_eolica.append(round(previsao_eolica))

    return previsao_solar, previsao_eolica