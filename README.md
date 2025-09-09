# 🚀 Atividade Remota de Python

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

Este projeto acadêmico aplica conceitos fundamentais de Python para resolver dois problemas principais:
1.  **Análise Estatística Pura:** Implementação de funções estatísticas do zero.
2.  **Análise de Dados de Vinhos:** Análise e visualização de um dataset sobre a qualidade de vinhos.
3.  **Consumo de API:** Interação com a PokeAPI para buscar e processar dados de Pokémon.

---

## 📂 Estrutura do Projeto

Cada arquivo neste repositório tem um propósito específico:

| Arquivo                  | Descrição                                                                              |
| ------------------------ | -------------------------------------------------------------------------------------- |
| `main.py`                | Script principal que analisa o `wine_quality.csv` e gera os gráficos.                  |
| `puras.py`               | Contém as implementações de funções estatísticas (média, mediana, moda, iqr) sem bibliotecas externas. |
| `pokeAPI.py`             | Script para buscar dados da PokeAPI, processar o JSON e salvar em CSV.                 |
| `wine_quality.csv`       | Dataset com dados sobre a qualidade de vinhos.                                         |
| `game_index_pokemon.csv` | Arquivo CSV gerado com os dados da PokeAPI.                                            |
| `histograma_alcool.png`  | Gráfico gerado mostrando a distribuição do teor alcoólico dos vinhos.                    |
| `boxplot_ph.png`         | Gráfico gerado mostrando a distribuição do pH dos vinhos.                              |

---

## ✨ Funcionalidades

-   **Análise de Dados:** Leitura, processamento e análise de dados tabulares com a biblioteca Pandas.
-   **Visualização de Dados:** Criação de gráficos informativos (histograma e boxplot) para entender a distribuição dos dados.
-   **Interação com API:** Requisições HTTP para uma API pública (`PokeAPI`), tratamento de erros e parsing de JSON.
-   **Funções Puras:** Demonstração de conhecimento de lógica de programação com a criação de funções estatísticas complexas do zero.

---

## 📊 Resultados e Visualizações

Parte fundamental do projeto foi gerar visualizações para entender melhor o dataset dos vinhos.

### Histograma do Teor Alcoólico
Este gráfico mostra a frequência de diferentes níveis de álcool nos vinhos analisados.

![Histograma do Teor Alcoólico](https://github.com/jphneves/PythonAtividadeRemota/blob/main/imgs/histograma_alcool.png)

### Boxplot do pH
Este gráfico resume a distribuição do pH, mostrando a mediana, os quartis e possíveis outliers.

![Boxplot do pH](https://github.com/jphneves/PythonAtividadeRemota/blob/main/imgs/boxplot_ph.png)

---

## 🛠️ Como Executar o Projeto

1.  **Clone o repositório:**
    ```bash
    # No console digite:
    git clone https://github.com/jphneves/PythonAtividadeRemota.git

    # Entre na pasta baixada:
    cd PythonAtividadeRemota
    ```

2.  **Instale as dependências:**
    ```bash
    pip install pandas requests matplotlib seaborn
    ```

3.  **Execute os scripts:**
    ```bash

    # DENTRO DA PASTA src/
    
    # Para rodar a análise de vinhos e gerar os gráficos
    python main.py

    # Para rodar funções python puras
    python puras.py

    # Para buscar os dados da PokeAPI
    python pokeAPI.py
    ```

---

## 👨‍💻 Autores

Projeto desenvolvido por:

* **João Pedro H Neves**
* **Davi Fiori**

---

**Universidade FAG - TOLEDO** *Curso de Engenharia de Software* *6º Período - 2025*
