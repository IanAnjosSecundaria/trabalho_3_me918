"""
Código base passado pelo professor só que em python
"""

import numpy as np
import pandas as pd
import random


from configuracoes import PASTA_DADOS, NOME_BD, momento_registro

def gerar_dados() -> None:
    ra = 172483
    random.seed(ra)
    np.random.seed(ra)

    b0:float = np.random.uniform(-2, 2)
    b1:float = np.random.uniform(-2, 2)
    bB = 2
    bC = 3
    n = 25

    x:list = np.random.poisson(4, n) + np.random.uniform(-3, 3, n)
    grupo:list = np.random.choice(["A", "B", "C"], size = n, replace = True)
    y:list = np.random.normal(loc = b0 + b1*x + bB*(grupo == "B") + bC*(grupo == "C"), scale = 2, size = n)

    # Criar o dataframe
    df = pd.DataFrame({
        "x": x,
        "grupo": grupo,
        "y": y,
        "momento_registro": [momento_registro()] * n
    })

    # Escrever o dataframe em um arquivo CSV
    df.to_csv(f"{PASTA_DADOS}/{NOME_BD}", index = False)

if __name__ == "__main__":
    gerar_dados()
