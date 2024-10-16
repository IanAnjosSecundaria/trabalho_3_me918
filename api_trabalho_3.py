"""
API trabalho 3
"""
# Bibliteca para API
from flask import Flask, request, jsonify, render_template_string

# Bibliotecas próprias
from configuracoes import momento_registro
from logica_api import obter_banco_de_dados, conferir_parametros, salvar_banco_de_dados, plot
from free_regression import Regression, generate_regression, transpose

from log import print_log
print = print_log

app = Flask(__name__)

# Funções para API:

@app.route("/")
def home():
    """
    Tela inicial da API
    """
    return "API TRABALHO 3 de ME918", 200

@app.route("/dados")
def ver_dados():
    """
    Ver o dicionário de dados atual

    Exemplo:
        curl http://127.0.0.1:5000/dados

    Exemplo (no próprio browser)
    """
    return globals()["BD_GLOBAL"], 200

@app.route("/treinar", methods = ["POST"])
def treinar_item():
    """
    Treina o banco de dados

    Exemplo:
        curl -X POST -H "Content-Type: application/json" \
        http://127.0.0.1:5000/treinar
    """
    dados = transpose([list(map(float, BD_GLOBAL["x"])), list(map(float, BD_GLOBAL["y"]))])
    REGRESSAO_GLOBAL.run(dados)
    return jsonify({"mensagem": "Requisição completa!"}), 200

@app.route("/inserir", methods = ["POST"])
def inserir_item():
    """
    Adiciona um item ao banco de dados

    Exemplo:
        curl -X POST -H "Content-Type: application/json" \
        -d '{"x": 3.15, "grupo": "A", "y": 51}' \
        http://127.0.0.1:5000/inserir
    """
    novo_item:dict = request.json
    colunas_necessarias = ["x", "grupo", "y"]

    if conferir_parametros(dados = novo_item, colunas = colunas_necessarias):
        globals()["BD_GLOBAL"]["x"].append(str(novo_item["x"]))
        globals()["BD_GLOBAL"]["grupo"].append(str(novo_item["grupo"]))
        globals()["BD_GLOBAL"]["y"].append(str(novo_item["y"]))
        globals()["BD_GLOBAL"]["momento_registro"].append(momento_registro())
        return jsonify({"mensagem": "Item adicionado com sucesso!"}), 201

    return jsonify({"erro": "Dados inválidos"}), 200
@app.route("/deletar", methods = ["POST"])
def deletar_item():
    """
    Deleta um item do banco de dados

    Exemplo:
        curl -X POST -H "Content-Type: application/json" \
        -d '{"coluna": 2}' \
        http://127.0.0.1:5000/deletar
    """
    requisicao = request.get_json()
    
    if "coluna" in requisicao:
        coluna = requisicao["coluna"]
        if coluna < len(globals()["BD_GLOBAL"]["x"]):
            for key in globals()["BD_GLOBAL"].keys():
                globals()["BD_GLOBAL"][key].pop(coluna)
            return jsonify({"mensagem": f"Coluna {coluna} deletada com sucesso!"}), 200
        return jsonify({"erro": "Coluna não encontrada"}), 404

    return jsonify({"erro": "Requisição incorreta, passe 'coluna' no corpo JSON!"}), 400

@app.route("/salvar", methods = ["POST"])
def salvar_bd():
    """
    Treina o banco de dados

    Exemplo:
        curl -X POST http://127.0.0.1:5000/salvar
    """
    if salvar_banco_de_dados(globals()["BD_GLOBAL"]):
        return jsonify({"mensagem": "Requisição de salvamento completa!"}), 200
    return jsonify({"erro": "Não foi possível salvar os dados!"}), 400

@app.route("/grafico", methods = ["GET"])
def obter_grafico():
    """
    Obter o gráfico mapeando X e Y, os grupos e uma reta de regressão

    Exemplo (no próprio browser):
        http://127.0.0.1:5000/grafico
    """
    plot_img = plot(dados = globals()["BD_GLOBAL"], b0 = globals()["REGRESSAO_GLOBAL"]["b"], b1 = globals()["REGRESSAO_GLOBAL"]["b_1"])
    
    # Renderizando a imagem no HTML como base64
    html = f'<img src="data:image/png;base64,{plot_img}"/>'
    return render_template_string(html), 200

@app.route("/parametros", methods = ["GET"])
def obter_estimativas_parametros():
    """
    Retorna um dicionario json com os parâmetros e regressores

    Exemplo (no próprio browser):
        http://127.0.0.1:5000/grafico

    Exemplo:
        curl http://127.0.0.1:5000/parametros
    """
    parametros = {}
    parametros["regressores"] = REGRESSAO_GLOBAL.regressors
    for parametro in REGRESSAO_GLOBAL.params:
        parametros[parametro] = REGRESSAO_GLOBAL[parametro]

    return jsonify(parametros), 200

@app.route("/predicao", methods = ["GET"])
def obter_predicao():
    """
    Faz uma predição, retornando um valor Y, aceita multiplas requisições

    Exemplo:
        curl -X GET -H "Content-Type: application/json" \
        -d '{"predicao": [3.1]}' \
        http://127.0.0.1:5000/predicao
    """
    requisicao = request.get_json()
    if "predicao" in requisicao.keys():
        predizer:list = requisicao["predicao"]
        if type(predizer[0]) != list:
            predizer = [predizer]
        resposta:list = REGRESSAO_GLOBAL.prediction(predizer)
        return jsonify(resposta), 200

    return jsonify({"erro": "Requisição incorreta, passe a lista de listas de predições chamada 'predicao'!"}), 400


if __name__ == "__main__":
    BD_GLOBAL = obter_banco_de_dados()

    REGRESSAO_GLOBAL = Regression(*generate_regression(regressors = 1, degree = 1))
    REGRESSAO_GLOBAL.set_seed(2024)
    dados = transpose([list(map(float, BD_GLOBAL["x"])), list(map(float, BD_GLOBAL["y"]))])
    REGRESSAO_GLOBAL.run(dados)

    app.run(debug=True)
