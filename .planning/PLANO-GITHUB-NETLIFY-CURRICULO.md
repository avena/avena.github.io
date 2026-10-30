# Plano: GitHub + Netlify + Currículo atualizado

## Objetivo
1. Deixar o portfólio (`avena.github.io`) publicado no GitHub e Netlify.
2. Adicionar o projeto **clima_litoralsul** (https://github.com/avena/clima_litoralsul, https://climalitoralsul.netlify.app/) como projeto no currículo.
3. Atualizar o currículo com os dados fornecidos pelo Fernando (nome, email, telefone, LinkedIn, objetivo, histórico profissional, idiomas).
4. Verificar/scripts `start.sh` (visual local) e `deploy.sh` (deploy) do `clima_litoralsul`.

## Contexto atual
- `avena.github.io`: portfólio multi-idioma (pt/en/es), Bootstrap 5.3 + SASS, já em branch `felipegazolla`. Remote GitHub ainda não confirmado.
- `clima_litoralsul` (`~/clima_litoralsul`): SPA React + Tailwind, Python stdlib para coleta CIIAGRO. Já possui:
  - `start.sh` — exporta dados, builda Vite, serve `http.server` em porta livre (`--dev` para hot reload).
  - `deploy.sh` — `relatorio.py` + testes + `npm run check` + build, commita `dados.json` + PDFs e `git push` (o push é o deploy).
  - `netlify.toml` — `base = "site"`, `command = "npm run build"`, `publish = "dist"`.
  - `netlify.readme.md` — passo a passo da Netlify (Base directory = `site`).
  - Produção já aponta para `https://climalitoralsul.netlify.app/`.

## Issues (a criar no GitHub do avena.github.io)

| # | Issue | Escopo |
|---|-------|--------|
| 1 | Confirmar remote GitHub e publicar avena.github.io na Netlify | `git remote -v`, conectar repo, build command vazio, publish `css`/raiz |
| 2 | Adicionar projeto clima_litoralsul ao currículo (pt/en/es) | Card de projeto nos 3 `index.html` + `personal_data/projetos/` |
| 3 | Atualizar dados de contato (email, telefone, LinkedIn) | `contato.md`, footer, hero, `mailto:` nos 3 idiomas |
| 4 | Atualizar Objetivo e Histórico profissional | `trajetoria.md` + nova seção de currículo (pt/en/es) |
| 5 | Adicionar idiomas (Inglês/Espanhol) ao currículo | nova seção Idiomas nos 3 idiomas |
| 6 | Verificar start.sh e deploy.sh do clima_litoralsul | rodar localmente, validar build e deploy |

## Tarefas detalhadas

### T1 — Publicar no GitHub e Netlify (avena.github.io)
- [ ] Confirmar `git remote -v` aponta para `github.com/avena/avena.github.io` (ou criar).
- [ ] Conectar o repositório na Netlify.
- [ ] Build command: vazio (site estático HTML, sem build step) ou `npm run sass:build` se quiser compilar SASS no deploy.
- [ ] Publish directory: raiz (`.`) — não há `site/` com `package.json` como no clima_litoralsul.
- [ ] Verificar deploy em `https://avena.github.io/` (ou domínio custom).

### T2 — Projeto clima_litoralsul no currículo
- [ ] Criar entrada em `personal_data/projetos/clima_litoralsul.md` (pt).
- [ ] Refletir em `en/projetos/` e `es/projetos/` (mesma estrutura de espelhamento dos outros projetos).
- [ ] Adicionar card na seção Projetos dos 3 `index.html` (pt/en/es) com link para `https://climalitoralsul.netlify.app/` e `https://github.com/avena/clima_litoralsul`.
- Tags: AgroTech, Clima, Python, React, Dados Abertos.

### T3 — Contato atualizado
- [ ] `personal_data/contato.md`: email `fernando.avena@gmail.com`, telefone `(15) 99851-8542`, LinkedIn mantido.
- [ ] Footer dos 3 HTMLs: `mailto:fernando.avena@gmail.com`.
- [ ] Hero/CTA: link Currículo com o email correto.

### T4 — Objetivo + Histórico profissional (currículo)
- [ ] Escrever seção Objetivo (Engenheiro Agrônomo, ATER, agricultura digital, georreferenciamento, IA, CNH B).
- [ ] Reescrever `trajetoria.md` com os 5 cargos fornecidos (SA Consultoria 08/2025–Presente, Autônomo 01/2018–Presente, Fundepag/IEA 11/2025–06/2026, Bureau Veritas/RHD 02/2025–08/2025, BASF 01/2017–06/2017).
- [ ] Refletir em en/es.

### T5 — Idiomas
- [ ] Seção Idiomas: Inglês (Leitura/Escuta Intermediário, Escrita/Conversação Iniciante), Espanhol (mesmo).

### T6 — Scripts do clima_litoralsul (verificação)
- [ ] Rodar `./start.sh` localmente e confirmar que a página abre em `localhost`.
- [ ] Rodar `./start.sh --dev` para hot reload.
- [ ] Revisar `deploy.sh`: confirma que commita `dados.json` + PDFs e faz `git push` (push = deploy).
- [ ] Confirmar `netlify.toml` com `base = "site"` está correto para o deploy na Netlify.

## Critérios de conclusão (Definition of Done)
- [ ] Portfólio acessível via Netlify (build passa).
- [ ] Projeto clima_litoralsul visível na seção Projetos em pt/en/es.
- [ ] Contato, objetivo, histórico e idiomas refletem os dados fornecidos.
- [ ] `start.sh` e `deploy.sh` do clima_litoralsul validados localmente.

## Pós-conclusão
- Mover este plano para `.planning/archive/` após todas as issues estarem fechadas.
