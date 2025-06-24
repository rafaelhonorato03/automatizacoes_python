# Coletor de Dados do GitHub e Enviador de E-mail

Este projeto coleta dados de um usuário do GitHub via API e envia as informações por e-mail através do Gmail.

## Funcionalidades

- Coleta dados de um usuário específico do GitHub via API REST
- Extrai informações como número de seguidores e seguindo
- Acessa automaticamente o Gmail
- Envia e-mail com as informações coletadas

## Arquivos

- `coletor_dados_github_enviador_gmail.py` - Script principal

## Como usar

1. Certifique-se de que o chromedriver está na pasta `../recursos/`
2. Configure suas credenciais de e-mail no script:
   - `email` - Seu e-mail do Gmail
   - `senha` - Sua senha do Gmail
   - `destinatário` - E-mail de destino
3. Execute o script: `python coletor_dados_github_enviador_gmail.py`

## Dependências

- selenium
- requests
- chromedriver

## Observações

- O script atualmente coleta dados do usuário "gabriel" no GitHub
- Para alterar o usuário, modifique a URL na linha: `requests.get(r"https://api.github.com./users/gabriel")` 