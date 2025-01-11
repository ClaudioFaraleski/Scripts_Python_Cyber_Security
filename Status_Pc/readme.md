# Parsing HTML Script

## Overview

Este script foi projetado para coletar informações sobre um determinado domínio, incluindo seus endereços IP e subdomínios. Os resultados são salvos em um arquivo JSON chamado `hosts_info.json`.

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library

Você pode instalar as bibliotecas necessárias usando pip:

```sh
pip install requests beautifulsoup4
```

## Usage

1. Clone o repositório ou baixe o arquivo de script `parsing.py`.
2. Abra um terminal ou prompt de comando.
3. Navegue até o diretório onde `parsing.py` está localizado.
4. Execute o script usando Python:

```sh
python parsing.py
```

5. Quando solicitado, insira o domínio sobre o qual deseja coletar informações (e.g., `example.com`).

## Example

```sh
Bem-vindo ao programa de coleta de informações de hosts.
EX de dominio: google.com - Não é necessario Digitar www
Digite o Dominio: example.com
Endereços IP para example.com: ['93.184.216.34']
Subdomínios encontrados: ['sub.example.com']
Endereços IP para sub.example.com: ['93.184.216.35']
```

## Output

O script irá gerar um arquivo JSON chamado `hosts_info.json` ino mesmo diretório, contendo as informações coletadas:

```json
{
    "example.com": ["93.184.216.34"],
    "sub.example.com": ["93.184.216.35"]
}
```

## Troubleshooting

- Certifique-se de ter uma conexão ativa com a Internet.
- Verifique se o nome de domínio está correto e acessível.
- Verifique se há erros de digitação no nome de domínio.