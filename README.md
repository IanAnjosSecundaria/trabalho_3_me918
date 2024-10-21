# trabalho_3_me918

API em Python utilizando *Flask*.

# Logs/Registros

A API salva os registros das requisições em uma pasta chamada ```logs§```, em arquivos identificados pela data de inicialização da API.

# Como usar

Para utilizar a API, é necessário ter o *Python* instalado, juntamente com o *venv* (ambiente virtual). Siga os passos abaixo para instalar as dependências descritas no arquivo ```bibliotecas.txt``` dentro da pasta ```bibliotecas_venv```:

1. Crie o ambiente virtual: ```python3 -m venv meu_ambiente```

2. Ative o ambiente virtual: ```source meu_ambiente/bin/activate```

3. Na pasta raiz do repositório, instale as bibliotecas necessárias: ```pip install -r bibliotecas_venv/bibliotecas.txt```

Após a instalação, execute o código ```api_trabalho_3.py``` no terminal. A API será iniciada no endereço local (127.0.0.1) e ficará acessível pela porta 5000. A partir desse momento, todas as funcionalidades estarão disponíveis para uso.

# Detalhes

Como a ferramenta foi construida para o trabalho e será acessada apenas no local host, as variáveis globais para criar os modelos são válidas, caso essa API fosse escalar, ou seja, mais pessoas usasem simutaneamente essa API, o designe/arquitetura de acesso da API deveria ser diferente.

# Funcionalidades

## /dados

Retorna um banco de dados global (dados_regressao). Esse banco contém valores de x, grupo e valores de y, além de registros de data/hora da inserção dos dados.

### Descrição

As variáveis do banco de dados são as seguintes:

- x: lista de valores x;

- grupo: variando entre A, B e C como possíveis grupos;

- y: lista de valores y;

-  momento_registro: onde estão registros de data/hora da inserção dos dados.


### Uso

```
curl http://127.0.0.1:5000/dados
```


## /treinar

### Descrição

Treina o modelo de regressão linear com os dados disponíveis no banco  utilizado. Utiliza os valores x e y para ajustar um modelo de regressão, que será usado posteriormente para predições.

### Uso

```
curl -X POST -H "Content-Type: application/json" \
http://127.0.0.1:5000/treinar
```


## /inserir

### Descrição

Insere um novo item no banco de dados global. É necessário fornecer os valores de x, grupo e y no corpo da requisição no formato JSON para inserir o novo item.

### Uso

```
curl -X POST -H "Content-Type: application/json" \
-d '{"x": 3.15, "grupo": "A", "y": 51}' \
http://127.0.0.1:5000/inserir
```

## /deletar

### Descrição

Remove uma linha do banco de dados, especificada pelo índice da coluna. O valor da linha a ser deletada é passado no corpo da requisição em formato JSON, então a linha selecionada será deletada.

### Uso

```
curl -X POST -H "Content-Type: application/json" \
-d '{"coluna": 2}' \
http://127.0.0.1:5000/deletar
```


## /salvar

### Descrição

### Uso

```
curl -X POST http://127.0.0.1:5000/salvar
```


## /grafico

### Descrição

Gera e retorna um gráfico visualizando os dados x e y, assim como a reta ajustada pelo modelo de regressão. 

### Uso

```
http://127.0.0.1:5000/grafico
```


## /parametros

### Descrição

Retorna os parâmetros ajustados do modelo de regressão após o treinamento, incluindo os coeficientes (regressores) e as constantes. Esses parâmetros são de suma importância para interpretar como o modelo ajusta os dados.

### Uso

```
curl http://127.0.0.1:5000/parametros
```


## /predicao

### Descrição

Permite fazer previsões com o modelo de regressão treinado. O valor da predição é passado no corpo da requisição JSON. Se forem passados múltiplos valores, o modelo também irá retornar as previsões correspondentes.

### Uso

```
curl -X GET -H "Content-Type: application/json" \
-d '{"predicao": [3.1]}' \
http://127.0.0.1:5000/predicao
```
