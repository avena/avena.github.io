# Anotações sobre o site de referência

## Multi-idioma
- Raiz (`/`) = português
- `/en` = inglês
- O Felipe provavelmente tem `/es` também
- O language switcher fica no header, destaca o idioma atual
- A home inglesa está em `/en/index.html` (ou o SSG gera `/en/index.html`)
- Sub-páginas como `/en/servicos` viram `/en/servicos.html`

## Abordagem técnica
- **Static Site Generator** (quase certeza): URLs limpas, sem .html
- Possível: Hugo (Go), 11ty/Eleventy (JS), ou Astro (JS)
- Geração a partir de Markdown com templates

## Para nosso projeto
1. **Começar com HTML puro** → depois migrar pra SSG
2. **Idioma padrão: português na raiz** (/) igual ao referência
3. **Manter Bootstrap 5** (já configurado)
4. **BrowserSync** para desenvolvimento (já configurado, `npm start`)
5. **Roteamento futuro** com `.htaccess` ou PHP (decisão postergada)

## Seções obrigatórias
- [x] Header com language switcher
- [x] Hero (título impactante + foto + CTAs)
- [x] Serviços (cards clicáveis)
- [x] Sobre (história pessoal)
- [x] Skills (grade por área)
- [x] Jornada (timeline)
- [x] Projetos (cards com tags)
- [x] Como trabalho (etapas)
- [x] Contato (CTAs)
- [x] Footer
- [ ] Sub-página de serviços detalhados
- [ ] Sub-página de projetos detalhados
