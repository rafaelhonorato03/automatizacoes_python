# Automações Python

Coleção de scripts de automação desenvolvidos em Python para diferentes tarefas.

## Estrutura do Projeto

```
automatizacoes_python/
├── verificador_dominios/          # Verificação de disponibilidade de domínios
│   ├── verificador_disponibilidade_dominios.py
│   ├── lista_dominios.xls
│   ├── resultado_verificacao.txt
│   └── README.md
├── coletor_github/                # Coleta de dados do GitHub e envio por e-mail
│   ├── coletor_dados_github_enviador_gmail.py
│   └── README.md
├── enviador_emails/               # Envio de e-mails via SMTP
│   ├── enviador_email_smtp.py
│   └── README.md
├── recursos/                      # Recursos compartilhados
│   ├── chromedriver.exe
│   ├── template_imports.py
│   └── README.md
├── requirements.txt               # Dependências do projeto
└── README.md
```

## Projetos Disponíveis

### 1. Verificador de Domínios
- **Localização**: `verificador_dominios/`
- **Função**: Verifica automaticamente a disponibilidade de domínios no registro.br
- **Arquivo principal**: `verificador_disponibilidade_dominios.py`

### 2. Coletor de Dados do GitHub
- **Localização**: `coletor_github/`
- **Função**: Coleta dados de usuários do GitHub via API e envia por e-mail
- **Arquivo principal**: `coletor_dados_github_enviador_gmail.py`

### 3. Enviador de E-mails
- **Localização**: `enviador_emails/`
- **Função**: Envia e-mails com anexos usando SMTP
- **Arquivo principal**: `enviador_email_smtp.py`

## Dependências Gerais

- Python 3.x
- selenium
- xlrd
- requests
- pandas

## Instalação

### Instalação Rápida
```bash
pip install -r requirements.txt
```

### Instalação Manual
```bash
pip install selenium xlrd requests pandas
```

## Como Usar

Cada projeto possui seu próprio README com instruções específicas. Navegue até a pasta do projeto desejado e siga as instruções no arquivo README.md correspondente.

## Recursos Compartilhados

A pasta `recursos/` contém arquivos compartilhados entre os projetos:
- `chromedriver.exe` - Driver do Chrome para automação web
- `template_imports.py` - Template com imports comuns

## Contribuição

Para adicionar novos projetos de automação:
1. Crie uma nova pasta com nome descritivo
2. Adicione um README.md explicando a funcionalidade
3. Atualize este README principal
4. Atualize o requirements.txt se necessário
