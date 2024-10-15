"""
Lógica da API
"""

from configuracoes import PASTA_DADOS, NOME_BD, momento_registro

from log import print_log
print = print_log

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

def salvar_banco_de_dados(dados:dict) -> bool:
    """
    Salva o banco de dados

    Se der certo retorna True, caso contrário retorna False
    """
    try:
        with open(f"{PASTA_DADOS}/{NOME_BD}", "w") as arq:
            arq.write(dados)
        print(f"Dados salvo em {PASTA_DADOS}/{NOME_BD}...")
        return True
    except:
        return False

def conferir_parametros(dados:dict, colunas:list) -> bool:
    """
    Confere se no dicionário
    """
    if set(dados.keys()) & set(colunas) == set(dados.keys()):
        return True
    return False

