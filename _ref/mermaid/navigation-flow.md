# Diagrama de Fluxo de Navegação

```mermaid
flowchart TD
    A[Hero: From the field to code.] --> B[Services: What I build.]
    B --> C[Service cards] --> D[/en/servicos full page]
    A --> E[About: Background story]
    E --> F[Skills grouped by area]
    F --> G[Journey timeline]
    G --> H[Featured projects]
    H --> I[/en/projetos full gallery]
    A --> J[How I work process steps]
    J --> K[Contact: Let's talk]
    K --> L[Contact form / LinkedIn]
    A --> M[Recruiter cue: Résumé / LinkedIn]

    subgraph "Language Switch"
        PT[Português /] --> EN[English /en]
        EN --> PT
    end
```
