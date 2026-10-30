# Clima Litoral Sul — série climática

## Sobre
Painel com a série climática dos 17 municípios da mesorregião Litoral Sul Paulista (microrregiões de Itanhaém e Registro), a partir das estações do CIIAGRO. Desenvolvido no programa ATER, com PDF de ficha por estação para ajudar no entendimento do clima da região.

## O projeto
- Coleta de dados em Python 3.12 (somente stdlib: `urllib`, `sqlite3`, `re`, `json`)
- Banco SQLite com 23 estações e cobertura de 1990 a 2026 (13 dos 17 municípios têm estação)
- SPA React + Tailwind v4, buildado com Vite, deploy estático na Netlify
- Climatogramas, médias mensais, distribuição sazonal da chuva e ranking de chuva anual
- Fichas em PDF (uma página por estação, A4, preto e branco)

## Tecnologias envolvidas
- Python, SQLite, React, Tailwind CSS, Vite, Netlify

## Como acessar
- Painel: https://climalitoralsul.netlify.app/
- Código: https://github.com/avena/clima_litoralsul
