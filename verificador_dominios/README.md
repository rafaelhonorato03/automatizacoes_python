# Verificador de Disponibilidade de Domínios

Este projeto automatiza a verificação de disponibilidade de domínios no site registro.br.

## Funcionalidades

- Lê uma lista de domínios de um arquivo Excel (`lista_dominios.xls`)
- Acessa automaticamente o site registro.br
- Verifica a disponibilidade de cada domínio da lista
- Salva os resultados em um arquivo de texto (`resultado_verificacao.txt`)

## Arquivos

- `verificador_disponibilidade_dominios.py` - Script principal
- `lista_dominios.xls` - Lista de domínios para verificar
- `resultado_verificacao.txt` - Resultado da verificação

## Como usar

1. Certifique-se de que o chromedriver está na pasta `../recursos/`
2. Coloque os domínios que deseja verificar no arquivo `lista_dominios.xls`
3. Execute o script: `python verificador_disponibilidade_dominios.py`

## Dependências

- selenium
- xlrd
- chromedriver 