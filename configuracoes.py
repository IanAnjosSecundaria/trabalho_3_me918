"""
Arquivo de configurações estáticas globais
"""
from datetime import datetime

PASTA_DADOS = "dados"
NOME_BD = "dados_regressao.csv"

def momento_registro() -> str:
    """
    Retorna o ano, mês, dia, minuto e segundo do momento do registro.
    """
    agora = datetime.now()
    ano = agora.year
    mes = agora.month
    dia = agora.day
    hora = agora.hour
    minuto = agora.minute
    segundo = agora.second
    return f"{ano}-{mes}-{dia} {hora}:{minuto}:{segundo}"
