# Aurora Siger - Sistema de Gerenciamento Inteligente da Colônia (FASE 3)

Este projeto foi desenvolvido com foco nas disciplina de **Lógica e Estrutura de Dados**, representando o funcionamento inteligente de uma colônia espacial. O sistema integra organização de dados, tomada de decisão baseada em regras, modelos matemáticos de previsão e análise energética.

## 🚀 Funcionamento

O sistema opera de forma integrada processando quatro pilares principais:

1.  **Organização de Dados:** Utiliza estruturas eficientes (listas e dicionários) para representar o estado da colônia e sua hierarquia de sistemas.
2.  **Lógica de Decisão:** Aplica regras para gerenciar o consumo de energia, priorizando sistemas críticos como o **Suporte à Vida**.
3.  **Modelo de Previsão:** Utiliza regressão linear simples para estimar a geração de energia futura com base na velocidade do vento.
4.  **Análise Energética:** Compara a geração em tempo real com o consumo para sugerir ações (armazenamento ou economia).

## 📂 Estrutura do Projeto

- `main.py`: Ponto de entrada que coordena a execução de todos os módulos.
- `dados_colonia.py`: Armazena as estruturas de dados (listas de histórico e dicionário de sistemas).
- `regras_decisao.py`: Contém a lógica de IF/ELSE e a priorização de subsistemas.
- `modelo_previsao.py`: Implementa o cálculo matemático de previsão (regressão).
- `analise_energetica.py`: Analisa o equilíbrio entre geração e consumo.

## 📑 Exemplo de Entrada e Saída

### Entrada (configurada em `dados_colonia.py`)
- Energia Atual: 40
- Consumo Atual: 70
- Vento Histórico: `[8, 10, 12]`
- Energia Histórica: `[20, 25, 30]`

### Saída (Console)
```text
[PASSO 1] Verificando Regras de Decisão...
ALERTA CRÍTICO: Ativar modo economia extrema.
Ação: Desligando sistemas não essenciais...
  > Sistema 'energia' operando em modo reduzido.
  > Sistema 'suporte_vida' MANTIDO (Prioridade Máxima).

[PASSO 2] Analisando Uso de Energia...
ALERTA: consumo maior que geração

[PASSO 3] Executando Modelo de Previsão...
Previsão para vento de 11 m/s: 27.5 unidades de energia
```

---
*Projeto desenvolvido como parte da atividade detalhada da fase 3.*
