# avena.github.io

Portfólio pessoal multi-idioma (**pt / en / es**) de Fernando Padilha Avena, com a documentação do **LTSP** convertida de PmWiki para HTML estático.

- **GitHub:** https://github.com/avena/avena.github.io
- **GitHub Pages:** https://avena.github.io/
- **Netlify:** deploy a partir deste repositório (branch `paleta-agro`)

## Estrutura

| Caminho | O que é |
|---|---|
| `/index.html` | versão em português |
| `/en/index.html` | versão em inglês |
| `/es/index.html` | versão em espanhol |
| `/personal_data/` | conteúdo textual separado por seção (`.md`) |
| `/ltsp/` | documentação LTSP estática (73 páginas HTML) |
| `/scss/styles.scss` | estilos personalizados (fonte do CSS) |
| `/css/styles.css` | **gerado pelo SASS — não editar direto** |
| `/js/script.js` | efeito typing + language switcher |
| `/_convert_ltsp.py` | conversão PmWiki → HTML (re-geração) |

## Comandos

| Comando | O que faz |
|---|---|
| `npm run sass:build` | Compila SCSS → CSS |
| `npm run sass:watch` | Watch do SCSS |
| `npm start` | BrowserSync na porta 3000 com livereload |
| `npm run watch` | Sass watch + BrowserSync simultâneo |

## Stack

Bootstrap 5.3, Font Awesome 7, SASS e JavaScript puro (sem framework). Deploy estático servido por GitHub Pages e Netlify.

## Projetos destacados

- **Clima Litoral Sul** — série climática dos 17 municípios do Litoral Sul Paulista, com painel web e fichas em PDF. https://climalitoralsul.netlify.app/ · https://github.com/avena/clima_litoralsul
- **Documentação LTSP em português** — `/ltsp/`
- **Coleta de Dados de Campo (Power Apps)** — protótipo de app de coleta

## Convenções

- Os três HTMLs (`index.html`, `en/index.html`, `es/index.html`) espelham as mesmas seções.
- O language switcher mostra apenas os outros idiomas (sem self-link).
- Commits só após autorização explícita (ver `AGENTS.md`).
