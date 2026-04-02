# Scripts de Formatação MkDocs

Este diretório contém scripts para manter a formatação consistente dos arquivos Markdown do projeto Ser Empreendedor.

## 📋 Scripts Disponíveis

### 1. `fix-admonition-lists.py` - Correção Automática

Corrige problemas de formatação em listas dentro de admonitions (???/!!! blocks).

**Problema resolvido:**
Listas numeradas ou com marcadores dentro de admonitions precisam de uma linha em branco antes para renderizar corretamente no MkDocs Material.

**Uso:**
```bash
# Verificar quais arquivos precisam de correção (não modifica)
python3 scripts/fix-admonition-lists.py --dry-run docs/

# Corrigir todos os arquivos na pasta docs/
python3 scripts/fix-admonition-lists.py docs/

# Corrigir um arquivo específico
python3 scripts/fix-admonition-lists.py docs/painel.md

# Validar um arquivo específico (modo detalhado)
python3 scripts/fix-admonition-lists.py --validate docs/painel.md

# Ajuda
python3 scripts/fix-admonition-lists.py --help
```

### 2. `validate-admonitions.py` - Validação Contínua

Verifica se há problemas de formatação nos arquivos. Ideal para usar em pre-commit hooks ou CI/CD.

**Uso:**
```bash
# Validar todos os arquivos na pasta docs/
python3 scripts/validate-admonitions.py

# Validar pasta específica
python3 scripts/validate-admonitions.py docs/rituais/

# Ajuda
python3 scripts/validate-admonitions.py --help
```

**Códigos de saída:**
- `0`: Todos os arquivos estão OK
- `1`: Foram encontrados problemas

## 🔄 Workflow Recomendado

### Antes de Commitar
```bash
# 1. Valide se há problemas
python3 scripts/validate-admonitions.py

# 2. Se houver problemas, corrija automaticamente
python3 scripts/fix-admonition-lists.py docs/

# 3. Verifique se está tudo OK
python3 scripts/validate-admonitions.py
```

### Pre-commit Hook (Opcional)

Adicione ao seu `.git/hooks/pre-commit`:
```bash
#!/bin/sh
python3 scripts/validate-admonitions.py
exit $?
```

## 🐛 Padrões Corrigidos

### Padrão 1: "**O que fazer:**" + Lista
**Antes (quebra renderização):**
```markdown
??? abstract "Título"
    **O que fazer:**
    1. Primeiro item
    2. Segundo item
```

**Depois (correto):**
```markdown
??? abstract "Título"
    **O que fazer:**
    
    1. Primeiro item
    2. Segundo item
```

### Padrão 2: Texto com ":" + Lista
**Antes:**
```markdown
??? question "Pergunta"
    Você pode usar:
    - Opção 1
    - Opção 2
```

**Depois:**
```markdown
??? question "Pergunta"
    Você pode usar:

    - Opção 1
    - Opção 2
```

### Padrão 3: "Adapte:" + Lista
**Antes:**
```markdown
??? question "E se for pequeno?"
    Adapte:
    - Estrutura: Simplificada
    - Processos: Manuais
```

**Depois:**
```markdown
??? question "E se for pequeno?"
    Adapte:

    - Estrutura: Simplificada
    - Processos: Manuais
```

## 📊 Estatísticas do Projeto

Na última execução (2 abr 2026):
- **15 arquivos markdown** verificados
- **13 arquivos** precisaram de correção
- **2 arquivos** já estavam OK
- **0 problemas** restantes após correção

## 🔧 Manutenção

### Para Adicionar Novos Padrões
Edite `fix-admonition-lists.py` e adicione novos padrões na função `fix_specific_patterns()`.

### Para Testar
```bash
# Teste em modo dry-run primeiro
python3 scripts/fix-admonition-lists.py --dry-run docs/

# Verifique um arquivo específico
python3 scripts/fix-admonition-lists.py --validate docs/seu-arquivo.md
```

## 🚨 Importante

- **Sempre faça backup** antes de executar correções em massa
- **Use `--dry-run`** primeiro para ver o que será alterado
- **Teste localmente** após as correções para garantir que a renderização está correta
- **Commit separado** para correções de formatação (facilita review)

## 📚 Referências

- [MkDocs Material Documentation](https://squidfunk.github.io/mkdocs-material/)
- [Admonitions Syntax](https://squidfunk.github.io/mkdocs-material/reference/admonitions/)
- [List Syntax](https://squidfunk.github.io/mkdocs-material/reference/lists/)
