# Recursos Compartilhados

Esta pasta contém arquivos e recursos compartilhados entre os diferentes projetos de automação.

## Arquivos

- `chromedriver.exe` - Driver do Chrome para automação web com Selenium
- `template_imports.py` - Template com imports comuns para projetos de automação

## Como usar

### Chromedriver
- O chromedriver deve ser compatível com a versão do Chrome instalada
- Para atualizar, baixe a versão correspondente em: https://chromedriver.chromium.org/
- Os scripts referenciam este arquivo usando o caminho relativo `../recursos/chromedriver.exe`

### Template de Imports
- Use como base para novos projetos de automação
- Contém imports comuns como pandas, xlrd, selenium, requests
- Copie e adapte conforme necessário para seu projeto

## Manutenção

- Mantenha o chromedriver atualizado
- Verifique a compatibilidade com novas versões do Chrome
- Atualize o template de imports conforme necessário 