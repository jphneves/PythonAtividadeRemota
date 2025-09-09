import csv
import math
from collections import Counter


def media(data):
    return sum(data) / len(data)


def mediana(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        return sorted_data[mid]


def moda(data):
    counts = Counter(data)
    max_count = max(counts.values())
    modas = [key for key, value in counts.items() if value == max_count]
    return modas


def _percentil(data, percentile):
    size = len(data)
    sorted_data = sorted(data)
    k = (size - 1) * percentile
    f = math.floor(k)
    c = math.ceil(k)
    if f == c:
        return sorted_data[int(k)]
    d0 = sorted_data[int(f)] * (c - k)
    d1 = sorted_data[int(c)] * (k - f)
    return d0 + d1


def iqr(data):
    q1 = _percentil(data, 0.25)
    q3 = _percentil(data, 0.75)
    return q3 - q1


coluna_alcool = []
indice_da_coluna = 10

try:
    with open('wine_quality.csv', 'r') as arquivo_csv:
        leitor = csv.reader(arquivo_csv)

        next(leitor)

        for linha in leitor:
            try:
                valor = float(linha[indice_da_coluna])
                coluna_alcool.append(valor)
            except (ValueError, IndexError):
                continue

    print(f"--- Análise da coluna 'alcohol' do arquivo wine_quality.csv ---")
    if coluna_alcool:
        print(f"Média: {media(coluna_alcool)}")
        print(f"Mediana: {mediana(coluna_alcool)}")
        print(f"Moda: {moda(coluna_alcool)}")
        print(f"IQR: {iqr(coluna_alcool)}")
    else:
        print("Nenhum dado foi lido da coluna especificada.")

except FileNotFoundError:
    print("Erro: O arquivo 'wine_quality.csv' não foi encontrado.")