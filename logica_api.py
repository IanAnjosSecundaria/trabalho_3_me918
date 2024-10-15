"""
Lógica da API
"""

from configuracoes import PASTA_DADOS, NOME_BD, momento_registro

def obter_banco_de_dados() -> dict:
    """
    Lê o arquivo csv e retorna dicionario de listas
    """
    with open(f"{PASTA_DADOS}/{NOME_BD}", "r") as arq:
        dados = arq.read()

    dados = dados.split("\n")
    dados = [dados[i].split(",") for i in range(len(dados))][:-1]

    for i in range(len(dados)):
        print(f"{i} -> {'; '.join(dados[i])}")

    dados_dict = {}
    for col in range(len(dados[0])):
        dados_dict[dados[0][col]] = []
        for line in range(1, len(dados)):
            dados_dict[dados[0][col]].append(dados[line][col])

    return dados_dict

def conferir_parametros(dados:dict, colunas:list) -> bool:
    """
    Confere se no dicionário
    """
    if set(dados.keys()) & set(colunas) == set(dados.keys()):
        return True
    return False

