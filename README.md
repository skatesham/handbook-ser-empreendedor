# Ecocria Handbook 📚

Base de conhecimento interna da Ecocria construída em cima do [MkDocs Material](https://squidfunk.github.io/mkdocs-material/). Este repositório consolida rituais, processos e cultura para facilitar onboarding e aprendizado contínuo.

## Estrutura

```
.
├─ docs/
│  ├─ index.md                # Home e visão geral
│  ├─ ...                     # ...
│  └─ assets/                 # Logos, favicons e ilustrações
├─ mkdocs.yml                 # Configuração do site
└─ requirements.txt           # Dependências Python
```

## Pré-requisitos

- Python 3.10+
- `pip` atualizado

## Como rodar localmente

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

```bash
source .venv/bin/activate
mkdocs serve
```

Abra <http://127.0.0.1:8000> para visualizar o handbook com recarregamento automático.

## Publicação

1. Garanta que a branch principal está atualizada.
2. Valide o conteúdo (`mkdocs serve`) e corrija warnings.
3. Execute `mkdocs gh-deploy` para publicar no GitHub Pages configurado em `mkdocs.yml`.

## Contribuições

- Abra uma issue descrevendo contexto e motivação.
- Crie uma branch com suas mudanças.
- Envie um pull request com screenshots (quando pertinente) e resumo das alterações.

> Dúvidas? Procure o chapter owner de Documentação ou registre no canal `#handbook`.
