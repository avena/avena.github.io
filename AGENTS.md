# AGENTS.md

## Project
Portfolio pessoal multi-idioma (pt/en/es) de Fernando Padilha Avena, + documentação LTSP convertida de PmWiki para HTML estático.

Estrutura derivada de `felipegazolla.dev` com conteúdo real do LinkedIn.

## Commands

| Comando | O que faz |
|---|---|
| `npm run sass:build` | Compila SCSS → CSS |
| `npm run sass:watch` | Watch SCSS |
| `npm start` | BrowserSync na porta 3000 com livereload |
| `npm run watch` | Sass watch + BrowserSync simultâneo |

## Publicação (GitHub + Netlify)

- Repositório: https://github.com/avena/avena.github.io (branch `paleta-agro`).
- GitHub Pages: https://avena.github.io/ — deploy via Actions (`.github/workflows/pages.yml`), `build_type: workflow`. No ar.
- Netlify: **pendente** — conectar o repositório no painel (issue aberta #1). Build command vazio (HTML estático) ou `npm run sass:build`; publish directory `.` (raiz).
- Issues: https://github.com/avena/avena.github.io/issues
- Plano arquivado: `.planning/archive/PLANO-GITHUB-NETLIFY-CURRICULO.md`.

## Projeto clima_litoralsul (currículo)

- Repositório: `https://github.com/avena/clima_litoralsul` (em `~/clima_litoralsul`).
- Produção: `https://climalitoralsul.netlify.app/`.
- Scripts locais: `./start.sh` (serve a página localmente, `--dev` para hot reload) e `./deploy.sh` (push = deploy na Netlify).
- `netlify.toml`: `base = "site"`, `command = "npm run build"`, `publish = "dist"`.
- Deve ser adicionado como projeto no currículo (pt/en/es) com link para o app e o repo.


## Estrutura

- `/index.html` — raiz (português), `/en/index.html` — inglês, `/es/index.html` — espanhol
- `/scss/styles.scss` — estilos personalizados; compilar com `npm run sass:build`
- `/css/styles.css` — **não editar diretamente**, gerado pelo SASS
- `/js/script.js` — efeito typing + language switcher
- `/ltsp/` — docs LTSP estáticas, 71 páginas HTML convertidas
- `/personal_data/` — conteúdo textual separado por seção (`.md`)
- `/_convert_ltsp.py` — script de conversão PmWiki→HTML (mantido na raiz para re-geração)

## Commits

- **NUNCA** commitar sem perguntar primeiro. Sempre perguntar "posso commitar?" e aguardar resposta.
- Se houver muitas alterações (muitos arquivos, muitas inserções/linhas), avisar e sugerir que é um bom momento para commitar, mas sempre perguntar.
- Commits só depois de autorização explícita.

## Convenções

- Bootstrap 5.3 + Font Awesome 7 (ícones `fas`/`fab`) + SASS
- Cards com hover lift (`translateY(-4px)`) definido em `styles.scss`
- Timeline com linha vertical + dots + cards com borda esquerda colored
- Language switcher mostra apenas os outros idiomas (sem self-link)
- Footer com navegação + ícones sociais (GitHub, LinkedIn, email)
- Todos os 3 HTMLs (`index.html`, `en/index.html`, `es/index.html`) espelham as mesmas seções
- **Ordem das Seções:** Hero → Sobre → Carreira/Jornada → Habilidades (Skills) → Serviços → Projetos → Como Trabalho → Contato.
- **Grid de Habilidades (Skills):** 8 cards (`col-md-6 col-lg-4`). Em telas `lg` (3 colunas), a última linha tem 2 cards; o 7º card ("Produto & Domínio") usa `offset-lg-2` para centralizar a dupla no grid (offset 2 + 4 + 4 = 10 colunas, centralizado).
- **Grid de Projetos:** 4 cards com `col-md-6` (2 por linha em `md` e `lg`). Ordem padronizada nos 3 idiomas: 1. LTSP, 2. Clima Litoral Sul, 3. Sistema de Gestão Agrícola, 4. Coleta BASF (Power Apps). Botão "Ver todos os projetos" com `d-none`.
- **Contraste em fundos escuros:** O `$primary` da paleta agro (`#1E3F20`) é verde escuro. Em fundos escuros (hero, navbar, contact-section, footer), **nunca** usar texto na cor primária. Usar `$secondary` (`#D99B26`, dourado queimado) para títulos `text-primary`, hover de navbar e botões CTA de destaque, garantindo legibilidade e conformidade WCAG.

## Multi-idioma

- pt: `/` | en: `/en` | es: `/es`
- Navbar com `#` hash links para seções na página
- Active class no language switch via `updateActiveLang()` em `script.js`

## LTSP

- 73 arquivos HTML sob `/ltsp/` com header, sidebar, breadcrumb
- Sidebar: `<a href="/ltsp/">Página Inicial</a>` + links externos
- Navegação: `<a href="/" class="text-white-50 text-decoration-none">← Voltar ao currículo</a>`
- Links convertidos para caminhos relativos: `/ltsp/Main/Arquivo.html`
