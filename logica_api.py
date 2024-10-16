"""
Lógica da API
"""

# Bibliotecas para plot
import matplotlib.pyplot as plt
import io
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

# Bibliotecas próprias
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
    csv = ",".join(list(dados.keys())) + "\n"
    for i in range(len(dados[list(dados.keys())[0]])):
        csv += f"{dados['x'][i]},{dados['grupo'][i]},{dados['y'][i]},{dados['momento_registro'][i]}\n"
        
    try:
        with open(f"{PASTA_DADOS}/{NOME_BD}", "w") as arq:
            arq.write(csv)
        print(f"Dados salvo em {PASTA_DADOS}/{NOME_BD}...")
        return True
    except Exception as error:
        print(f"Erro em salvar os dados: {error}")
        return False

def conferir_parametros(dados:dict, colunas:list) -> bool:
    """
    Confere se no dicionário
    """
    if set(dados.keys()) & set(colunas) == set(dados.keys()):
        return True
    return False

def plot(dados:dict, b0:float, b1:float) -> "plot":
    """

    """
    fig, ax = plt.subplots()
    x = list(map(float, dados["x"]))
    y = list(map(float, dados["y"]))
    grupos = dados["grupo"]
    
    grupo_map = {g: i for i, g in enumerate(set(grupos))}
    grupos_numericos = [grupo_map[g] for g in grupos]

    scatter = ax.scatter(x, y, c = grupos_numericos, cmap = "viridis")

    x_g = [min(x), max(x)]
    y_g = [b0 + b1*min(x), b0 + b1*max(x)]
    ax.plot(x_g, y_g, linestyle = ":", label = f"Regressão Linear")

    # Convertendo o plot em uma imagem que o Flask pode servir
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    plt.close(fig)
    
    # Retornar a imagem como base64
    return base64.b64encode(output.getvalue()).decode("utf-8")
