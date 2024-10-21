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

### Descrição

### Uso

```
curl http://127.0.0.1:5000/dados
```


## /treinar

### Descrição

### Uso

```
curl -X POST -H "Content-Type: application/json" \
http://127.0.0.1:5000/treinar
```


## /inserir

### Descrição

### Uso

```
curl -X POST -H "Content-Type: application/json" \
-d '{"x": 3.15, "grupo": "A", "y": 51}' \
http://127.0.0.1:5000/inserir
```

## /deletar

### Descrição

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

### Uso

```
http://127.0.0.1:5000/grafico
```


## /parametros

### Descrição

### Uso

```
curl http://127.0.0.1:5000/parametros
```


## /parametros

### Descrição

### Uso

```
curl -X GET -H "Content-Type: application/json" \
-d '{"predicao": [3.1]}' \
http://127.0.0.1:5000/predicao
```
