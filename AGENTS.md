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

## Estrutura

- `/index.html` — raiz (português), `/en/index.html` — inglês, `/es/index.html` — espanhol
- `/scss/styles.scss` — estilos personalizados; compilar com `npm run sass:build`
- `/css/styles.css` — **não editar diretamente**, gerado pelo SASS
- `/js/script.js` — efeito typing + language switcher
- `/ltsp/` — docs LTSP estáticas, 71 páginas HTML convertidas
- `/personal_data/` — conteúdo textual separado por seção (`.md`)
- `/_convert_ltsp.py` — script de conversão PmWiki→HTML (mantido na raiz para re-geração)

## Convenções

- Bootstrap 5.3 + Font Awesome 7 (ícones `fas`/`fab`) + SASS
- Cards com hover lift (`translateY(-4px)`) definido em `styles.scss`
- Timeline com linha vertical + dots + cards com borda esquerda colored
- Language switcher mostra apenas os outros idiomas (sem self-link)
- Footer com navegação + ícones sociais (GitHub, LinkedIn, email)
- Todos os 3 HTMLs (`index.html`, `en/index.html`, `es/index.html`) espelham as mesmas seções

## Multi-idioma

- pt: `/` | en: `/en` | es: `/es`
- Navbar com `#` hash links para seções na página
- Active class no language switch via `updateActiveLang()` em `script.js`

## LTSP

- 73 arquivos HTML sob `/ltsp/` com header, sidebar, breadcrumb
- Sidebar: `<a href="/ltsp/">Página Inicial</a>` + links externos
- Navegação: `<a href="/" class="text-white-50 text-decoration-none">← Voltar ao currículo</a>`
- Links convertidos para caminhos relativos: `/ltsp/Main/Arquivo.html`
