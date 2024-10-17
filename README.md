# trabalho_3_me918

API em python usando *Flask*

# Logs/Registros

A API salva os registros dos pedidos a API na pasta log§ em arquivos que são indentificados pela data de inicialização da API.

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
