# 🚀 Ser Empreendedor — Handbook de Gestão

> **Aprenda gestão organizando sua empresa**: um sistema didático que ensina fundamentos de empreendedorismo enquanto estrutura seu negócio.

[![MkDocs](https://img.shields.io/badge/MkDocs-Material-526CFE?style=flat-square&logo=materialformkdocs)](https://squidfunk.github.io/mkdocs-material/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)

---

## 💡 O Que É Este Projeto?

O **Ser Empreendedor Handbook** é uma documentação interativa que guia pequenos empreendedores através de um sistema completo de gestão empresarial. Não é apenas teoria — é um **método prático** que você implementa enquanto aprende.

### 🎯 Principais Funcionalidades

- **📊 Painel Centralizado** — Visão consolidada de objetivo, pilares, estrutura e indicadores
- **🔄 Rituais Estruturados** — Trimestral, mensal, semanal e diário com etapas guiadas
- **📋 Quadro Kanban** — Gestão visual de ideias, problemas, decisões e prioridades
- **📈 Ferramentas de Gestão** — Indicadores, retrospectivas, gestão de crises e evolução contínua

### 🎁 Para Quem É?

- Pequenas empresas (1-20 pessoas)
- Empreendedores sem formação em gestão
- Negócios que precisam de estrutura sem burocracia
- Empresas que querem criar disciplina e continuidade

---

## 🏗️ Estrutura do Projeto

```
handbook-ser-empreendedor/
├── docs/
│   ├── index.md                    # Página inicial
│   ├── painel.md                   # Visão consolidada da empresa
│   ├── quadro.md                   # Gestão visual Kanban
│   ├── rituais/
│   │   ├── index.md                # Visão geral dos rituais
│   │   ├── trimestral.md           # Ritual trimestral (estratégia)
│   │   ├── mensal.md               # Ritual mensal (tático)
│   │   ├── semanal.md              # Ritual semanal (operação)
│   │   └── diario.md               # Ritual diário (coordenação)
│   ├── indicadores.md              # Métricas e KPIs
│   ├── retrospectivas.md           # Aprendizado contínuo
│   ├── crises.md                   # Gestão de problemas críticos
│   ├── evolucao.md                 # Melhoria contínua
│   └── assets/
│       ├── logo.png                # Logo do projeto
│       └── favicon.ico             # Favicon
├── mkdocs.yml                      # Configuração do MkDocs
├── requirements.txt                # Dependências Python
├── .gitignore                      # Arquivos ignorados
└── README.md                       # Este arquivo
```

---

## 🚀 Início Rápido

### Pré-requisitos

- **Python 3.10+** instalado
- **pip** atualizado
- **Git** (opcional, para clonar o repositório)

### Instalação

1. **Clone o repositório** (ou baixe o ZIP):

```bash
git clone https://github.com/skatesham/handbook-ser-emprendedor.git
cd handbook-ser-emprendedor
```

2. **Crie um ambiente virtual**:

```bash
python3 -m venv .venv
source .venv/bin/activate  # No Windows: .venv\Scripts\activate
```

3. **Instale as dependências**:

```bash
pip install -r requirements.txt
```

### Executar Localmente

```bash
mkdocs serve
```

Abra seu navegador em **http://127.0.0.1:8000** para visualizar o handbook com recarregamento automático.

---

## 📦 Publicação

### GitHub Pages (Recomendado)

1. **Configure o repositório** no GitHub
2. **Valide o conteúdo** localmente:

```bash
mkdocs serve
```

3. **Publique no GitHub Pages**:

```bash
mkdocs gh-deploy
```

O site será publicado em `https://<seu-usuario>.github.io/handbook-ser-emprendedor/`

### Outras Plataformas

- **Netlify**: Conecte o repositório e configure build command: `mkdocs build`
- **Vercel**: Similar ao Netlify
- **Cloudflare Pages**: Suporta MkDocs nativamente

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Versão | Descrição |
|------------|--------|-----------|
| [MkDocs](https://www.mkdocs.org/) | 1.6.0+ | Gerador de sites estáticos |
| [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) | 9.5.0+ | Tema moderno e responsivo |
| [PyMdown Extensions](https://facelessuser.github.io/pymdown-extensions/) | 10.8+ | Extensões Markdown avançadas |
| [Mermaid](https://mermaid.js.org/) | - | Diagramas e fluxogramas |

### Extensões Markdown Ativas

- ✅ Superfences (blocos de código avançados)
- ✅ Tabbed (conteúdo em abas)
- ✅ Admonitions (caixas de destaque)
- ✅ Details (conteúdo expansível)
- ✅ Emoji (suporte a emojis)
- ✅ Mermaid (diagramas)

---

## 📚 Estrutura de Conteúdo

### Navegação Principal

```yaml
🏠 Início                    # Visão geral do sistema
📊 Painel                    # Centralização de informações
🔄 Rituais                   # Gestão por cadência
  ├─ 🗓️ Trimestral          # Estratégia (2-4h/90 dias)
  ├─ 📅 Mensal               # Tático (1-2h/30 dias)
  ├─ 📆 Semanal              # Operação (30-60min/7 dias)
  └─ ☀️ Diário               # Coordenação (10-15min/dia)
📋 Quadro                    # Gestão visual Kanban
📈 Gestão                    # Ferramentas avançadas
  ├─ 📊 Indicadores          # Métricas e KPIs
  ├─ 🔍 Retrospectivas       # Aprendizado contínuo
  ├─ 🚨 Crises               # Gestão de problemas
  └─ ♻️ Evolução             # Melhoria contínua
```

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Siga estas etapas:

### 1. Reporte Problemas

Encontrou um erro ou tem uma sugestão? [Abra uma issue](https://github.com/skatesham/handbook-ser-emprendedor/issues) descrevendo:

- Contexto e motivação
- Comportamento esperado vs atual
- Screenshots (se aplicável)

### 2. Propondo Mudanças

1. **Fork** o repositório
2. **Crie uma branch** para sua feature:
   ```bash
   git checkout -b feature/minha-melhoria
   ```
3. **Faça suas alterações** e teste localmente
4. **Commit** suas mudanças:
   ```bash
   git commit -m "feat: adiciona seção sobre X"
   ```
5. **Push** para sua branch:
   ```bash
   git push origin feature/minha-melhoria
   ```
6. **Abra um Pull Request** com descrição detalhada

### 3. Padrões de Código

- Use Markdown semântico e limpo
- Mantenha consistência com o estilo existente
- Teste localmente antes de submeter
- Adicione screenshots para mudanças visuais

---

## 📝 Licença

Este projeto está sob a licença **MIT**. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 🙏 Agradecimentos

- [MkDocs](https://www.mkdocs.org/) pela ferramenta incrível
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) pelo tema excepcional
- Comunidade de pequenos empreendedores que inspirou este projeto

---

## 📞 Contato

- **Repositório**: [github.com/skatesham/handbook-ser-emprendedor](https://github.com/skatesham/handbook-ser-emprendedor)
- **Issues**: [Reporte problemas aqui](https://github.com/skatesham/handbook-ser-emprendedor/issues)
- **Documentação**: [Acesse o handbook completo](https://skatesham.github.io/handbook-ser-emprendedor/)

---

<p align="center">
  Feito com ❤️ para pequenos empreendedores que querem estruturar seus negócios
</p>

<p align="center">
  <strong>Ser Empreendedor</strong> — Aprenda gestão organizando sua empresa 🚀
</p>
