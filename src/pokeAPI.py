import requests
import pandas as pd


def baixar_e_processar_pokemon(pokemon_id):
    """
    Baixa os dados de um Pokémon da PokeAPI, processa os game_indices
    e salva em um arquivo CSV.
    """
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    nome_arquivo_csv = '../csv/game_index_pokemon.csv'

    print(f"Buscando dados para o Pokémon ID: '{pokemon_id}'...")

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            print("Download concluído com sucesso!")

            dados_pokemon = response.json()
            game_indices_lista = dados_pokemon.get('game_indices', [])

            if not game_indices_lista:
                print(f"O Pokémon ID '{pokemon_id}' não possui 'game_indices'. Nenhum arquivo foi criado.")
                return

            dados_para_df = []
            for indice in game_indices_lista:
                dados_para_df.append({
                    'game_index': indice.get('game_index'),
                    'version': indice.get('version', {}).get('name')
                })

            df = pd.DataFrame(dados_para_df)

            df.to_csv(
                nome_arquivo_csv,
                sep=';',
                encoding='utf-8',
                index=False
            )

            print(f"Arquivo '{nome_arquivo_csv}' salvo com sucesso!")
            print("\nPré-visualização dos dados salvos:")
            print(df.head())

        else:
            print(f"Erro ao buscar dados. A API retornou o status: {response.status_code}")

    except requests.exceptions.Timeout:
        print("Erro: A requisição demorou muito para responder (timeout). Tente novamente mais tarde.")
    except requests.exceptions.RequestException as e:
        print(f"Ocorreu um erro de conexão: {e}")


# --- Execução do Script com o ID 4 ---
baixar_e_processar_pokemon(4)