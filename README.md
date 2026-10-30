# avena.github.io Blueprint

## System Overview

Portfólio pessoal multi-idioma (**pt / en / es**) de Fernando Padilha Avena, construído com Bootstrap 5.3, Font Awesome 7, SASS e JavaScript nativo, acompanhado do acervo de documentação estática do **LTSP** (Linux Terminal Server Project) migrado de PmWiki para HTML.

- **GitHub:** https://github.com/avena/avena.github.io
- **GitHub Pages:** https://avena.github.io/
- **Netlify:** deploy contínuo via branch `paleta-agro`

## Local Interface & Invariants

Contém o utilitário de conversão e re-geração estática da base histórica do LTSP:
- `_convert_ltsp.py`:
  - `main()`: Processa os arquivos-fonte PmWiki em `ltsp/tar.gz.files/wiki.d` e gera páginas HTML estáticas na árvore `ltsp/`.
  - `extract(path: str) -> str | None`: Lê arquivos PmWiki em codificação ISO-8859-1 e extrai o corpo do texto desescapado.
  - `conv(text: str, sb: bool = False) -> str`: Converte marcação PmWiki (títulos, listas, blocos `<pre>`, divisórias) para elementos HTML.
  - `inline(t: str) -> str`: Transforma sintaxe inline (negrito, itálico, links externos e internos, código) em HTML.
  - `get_sidebar() -> str`: Lê e compila o menu de navegação a partir de `Site.SideBar`.
- **Local Invariants:**
  - A execução de `_convert_ltsp.py` requer a presença do diretório `ltsp/tar.gz.files/wiki.d`.
  - A codificação dos arquivos PmWiki de entrada é tratada como ISO-8859-1.
- **Local Side Effects:**
  - Cria e sobrescreve arquivos `.html` na árvore `/ltsp/` e `/ltsp/Main/`.

## Subdirectories & System Boundaries

- [Client Scripts (js)](./js/README.md): Utilitários client-side nativos (efeito typewriter e alternador de idiomas).
- `scss/`: Folhas de estilo Sass com a paleta agro e regras de layout responsivo (fonte de verdade de estilos).
- `css/`: CSS compilado via Dart Sass (`styles.css` não deve ser editado manualmente).
- `ltsp/`: Acervo documental com 73 páginas estáticas de documentação LTSP em português.
- `en/` & `es/`: Versões do portfólio em inglês e espanhol, espelhando a estrutura do `index.html`.
- `personal_data/`: Textos-fonte e dados de projetos em formato Markdown.

## Global Invariants

- **Espelhamento Multi-idioma:** As páginas `index.html`, `en/index.html` e `es/index.html` mantêm estrutura de seções, componentes de navegação e grids idênticos.
- **Ordem das Seções:** `Hero` → `Sobre` → `Carreira/Jornada` → `Habilidades (Skills)` → `Serviços` → `Projetos` → `Como Trabalho` → `Contato`.
- **Contraste de Acessibilidade:** Em fundos escuros (header, navbar, contact, footer), a cor primária escura (`#1E3F20`) nunca é utilizada em texto; utiliza-se a cor secundária dourada (`#D99B26`) para assegurar conformidade WCAG.
- **Isolamento de Estilos:** Edições visuais devem ser realizadas exclusivamente nos arquivos `.scss`, com compilação gerando `css/styles.css`.

## Global Side Effects

- **Deploy Automatizado:** Pushes na branch `paleta-agro` disparam o GitHub Actions para GitHub Pages e trigger no Netlify.
- **Compilação de CSS:** `npm run sass:build` sobrescreve `css/styles.css`.

## System Verification

- Run: `npm run sass:build`

---

## Estrutura & Referência

| Caminho | O que é |
|---|---|
| `/index.html` | Versão em português |
| `/en/index.html` | Versão em inglês |
| `/es/index.html` | Versão em espanhol |
| `/personal_data/` | Conteúdo textual separado por seção (`.md`) |
| `/ltsp/` | Documentação LTSP estática (73 páginas HTML) |
| `/scss/styles.scss` | Estilos personalizados (fonte do CSS) |
| `/css/styles.css` | **Gerado pelo SASS — não editar direto** |
| `/js/script.js` | Efeito typing + language switcher |
| `/_convert_ltsp.py` | Conversão PmWiki → HTML (re-geração) |

## Comandos

| Comando | O que faz |
|---|---|
| `npm run sass:build` | Compila SCSS → CSS |
| `npm run sass:watch` | Watch do SCSS |
| `npm start` | BrowserSync na porta 3000 com livereload |
| `npm run watch` | Sass watch + BrowserSync simultâneo |

## Projetos destacados

- **Clima Litoral Sul** — série climática dos 17 municípios do Litoral Sul Paulista, com painel web e fichas em PDF. https://climalitoralsul.netlify.app/ · https://github.com/avena/clima_litoralsul
- **Documentação LTSP em português** — `/ltsp/`
- **Coleta de Dados de Campo (Power Apps)** — protótipo de app de coleta
