# Enviador de E-mails via SMTP

Este projeto demonstra como enviar e-mails com anexos usando SMTP do Gmail.

## Funcionalidades

- Envia e-mails usando o protocolo SMTP
- Suporta anexos de arquivos
- Usa autenticação TLS para segurança
- Configurável para diferentes provedores de e-mail

## Arquivos

- `enviador_email_smtp.py` - Script principal

## Como usar

1. Configure suas credenciais no script:
   - `email` - Seu e-mail do Gmail
   - `s.login(fromaddr, 'robos123')` - Sua senha do Gmail
2. Modifique o assunto e corpo do e-mail conforme necessário
3. Execute o script: `python enviador_email_smtp.py`

## Dependências

- smtplib (biblioteca padrão do Python)
- email (biblioteca padrão do Python)

## Configurações de Segurança

Para usar com Gmail, você pode precisar:
- Ativar a verificação em duas etapas
- Gerar uma senha de aplicativo
- Usar a senha de aplicativo no lugar da senha normal

## Observações

- O script está configurado para Gmail (smtp.gmail.com, porta 587)
- Para outros provedores, ajuste o servidor SMTP e porta 